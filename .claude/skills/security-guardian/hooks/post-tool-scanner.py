#!/usr/bin/env python3
"""
Security Guardian - PostToolUse Hook

Runs after Write/Edit operations to:
1. Update iteration tracking
2. Perform comprehensive security scan
3. Log findings for audit trail

Hook Configuration (.claude/settings.json):
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/skills/security-guardian/hooks/post-tool-scanner.py\"",
            "timeout": 10000
          }
        ]
      }
    ]
  }
}

Exit Codes:
  0 - All checks passed
  1 - Non-blocking issues found (warning)
  (Does not return exit code 2 - post-tool is informational only)
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional

# Add scripts directory to path for imports
SCRIPT_DIR = Path(__file__).parent.parent / 'scripts'
sys.path.insert(0, str(SCRIPT_DIR))

try:
    from scanner import SecurityScanner, OutputFormatter, Severity
    from iteration_tracker import IterationTracker
except ImportError:
    # Fallback if imports fail - don't block
    SecurityScanner = None
    IterationTracker = None


class PostToolScanner:
    """Post-operation security scanning and tracking"""

    def __init__(self, project_root: Optional[Path] = None):
        if project_root is None:
            project_root = Path(os.environ.get('CLAUDE_PROJECT_DIR', Path.cwd()))

        self.project_root = Path(project_root).resolve()
        self.findings_log = self.project_root / '.security-guardian' / 'findings.json'

        # Initialize components if available
        self.scanner = SecurityScanner() if SecurityScanner else None
        self.tracker = IterationTracker(self.project_root) if IterationTracker else None

    def process(self, tool_name: str, tool_input: Dict, tool_output: Any) -> Dict:
        """Process a completed tool operation"""
        result = {
            "status": "success",
            "iteration_warning": None,
            "security_findings": [],
            "messages": []
        }

        file_path = tool_input.get('file_path', '')
        if not file_path:
            return result

        # Update iteration tracking
        if self.tracker:
            iteration_result = self.tracker.increment(file_path)
            result["iteration_info"] = iteration_result

            # Check if we need to show iteration warning
            if iteration_result.get('warning_level') in ['warning', 'high']:
                result["iteration_warning"] = iteration_result.get('message')
                result["messages"].append(iteration_result.get('message'))

        # Run security scan on the file
        if self.scanner and Path(file_path).exists():
            try:
                scan_result = self.scanner.scan(file_path)

                if scan_result.total_findings > 0:
                    result["security_findings"] = [
                        {
                            "id": f.id,
                            "name": f.name,
                            "severity": f.severity,
                            "line": f.line_number,
                            "description": f.description
                        }
                        for f in scan_result.findings
                    ]

                    # Record vulnerabilities in tracker
                    if self.tracker:
                        for finding in scan_result.findings:
                            self.tracker.add_vulnerability(file_path, finding.id)

                    # Format warning message for significant findings
                    high_plus = [f for f in scan_result.findings
                                if f.severity in ['CRITICAL', 'HIGH']]

                    if high_plus:
                        msg = self._format_findings_message(high_plus, file_path)
                        result["messages"].append(msg)

                    # Log findings
                    self._log_findings(file_path, scan_result.findings)

            except Exception as e:
                result["messages"].append(f"Security scan warning: {e}")

        return result

    def _format_findings_message(self, findings: List, file_path: str) -> str:
        """Format security findings for display"""
        lines = [
            "",
            "=" * 50,
            "🔍 SECURITY SCAN RESULTS",
            "=" * 50,
            f"File: {file_path}",
            f"Issues found: {len(findings)}",
            ""
        ]

        for f in findings[:5]:  # Limit to first 5
            icon = "🔴" if f.severity == "CRITICAL" else "🟠"
            lines.append(f"{icon} [{f.severity}] {f.name}")
            lines.append(f"   Line {f.line_number}: {f.description[:80]}...")
            if f.remediation:
                lines.append(f"   Fix: {f.remediation[:80]}...")
            lines.append("")

        if len(findings) > 5:
            lines.append(f"... and {len(findings) - 5} more issues")
            lines.append("")

        lines.append("Run '/security-guardian scan' for full details")
        lines.append("=" * 50)

        return "\n".join(lines)

    def _log_findings(self, file_path: str, findings: List):
        """Log findings to findings.json for audit trail"""
        try:
            self.findings_log.parent.mkdir(parents=True, exist_ok=True)

            # Load existing log
            existing = []
            if self.findings_log.exists():
                try:
                    with open(self.findings_log, 'r') as f:
                        existing = json.load(f)
                except:
                    existing = []

            # Add new findings
            timestamp = datetime.now(timezone.utc).isoformat()
            for finding in findings:
                entry = {
                    "timestamp": timestamp,
                    "file": file_path,
                    "id": finding.id,
                    "name": finding.name,
                    "severity": finding.severity,
                    "line": finding.line_number,
                    "cwe": finding.cwe if hasattr(finding, 'cwe') else ""
                }
                existing.append(entry)

            # Keep only last 1000 entries
            existing = existing[-1000:]

            # Save
            with open(self.findings_log, 'w') as f:
                json.dump(existing, f, indent=2)

        except Exception:
            pass  # Don't fail on logging errors


def main():
    """Main entry point for hook"""
    try:
        # Read input from stdin
        input_data = json.load(sys.stdin)

        tool_name = input_data.get('tool_name', '')
        tool_input = input_data.get('tool_input', {})
        tool_output = input_data.get('tool_output', {})

        # Only process Write and Edit tools
        if tool_name not in ['Write', 'Edit']:
            sys.exit(0)

        # Process the operation
        scanner = PostToolScanner()
        result = scanner.process(tool_name, tool_input, tool_output)

        # Output messages
        for message in result.get('messages', []):
            print(message, file=sys.stderr)

        # Track statistics
        if scanner.tracker:
            scanner.tracker.increment_stat('total_scans')
            if result.get('security_findings'):
                high_count = sum(1 for f in result['security_findings']
                               if f['severity'] in ['CRITICAL', 'HIGH'])
                if high_count > 0:
                    scanner.tracker.increment_stat('warnings_issued')

        # Always exit 0 or 1 for post-tool (don't block)
        if result.get('security_findings') or result.get('iteration_warning'):
            sys.exit(1)  # Warning
        else:
            sys.exit(0)  # Clean

    except json.JSONDecodeError:
        print("Error: Expected JSON input from Claude Code hook", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Security Guardian post-hook error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
