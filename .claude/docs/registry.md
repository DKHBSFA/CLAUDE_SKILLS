# Codebase Registry

**Last updated:** 2026-01-17

This is my memory. I update it as I learn. I check it before making claims.

---

## Skills

| Name | Location | Purpose |
|------|----------|---------|
| ux-craft | `.claude/skills/ux-craft/` | UI/UX development with distinctive design, accessibility, systematic enforcement |
| security-guardian | `.claude/skills/security-guardian/` | AI-specific security analysis for vibe coding vulnerabilities, OWASP Top 10, secrets, BaaS misconfigs |

### ux-craft Skill Structure

| File | Purpose |
|------|---------|
| `SKILL.md` | Core skill definition, workflow, commands |
| `directions.md` | 6 Design Directions with tokens and examples |
| `accessibility.md` | WCAG 2.2 AA/AAA compliance checklist |
| `typography.md` | Font stacks, scales, international support |
| `validation.md` | Pre/during/post generation validation rules |
| `examples/system-*.md` | Template design systems by direction |

### ux-craft Commands

| Command | Action |
|---------|--------|
| `/ux-craft establish` | Create system.md via direction selection |
| `/ux-craft apply` | Load system.md, enforce during generation |
| `/ux-craft audit` | Run validation checklist |
| `/ux-craft research [topic]` | Research-first workflow |
| `/ux-craft polish` | Apply "雕花" refinement |
| `/ux-craft extract [name]` | Save pattern to library |
| `/ux-craft compliance` | Audit and track design system compliance across codebase |
| `/ux-craft migrate [pattern]` | Systematically migrate pattern with tracking |

### security-guardian Skill Structure

| File | Purpose |
|------|---------|
| `SKILL.md` | Core skill definition, commands, detection patterns |
| `patterns/owasp-top-10.json` | 60+ OWASP vulnerability patterns |
| `patterns/secrets.json` | 40+ credential detection patterns |
| `patterns/baas-misconfig.json` | Supabase, Firebase, Amplify, PocketBase patterns |
| `scripts/scanner.py` | Core security scanning engine |
| `scripts/secret-detector.py` | Specialized secret detection |
| `scripts/baas-auditor.py` | BaaS configuration auditor |
| `scripts/iteration-tracker.py` | AI iteration tracking per file |
| `hooks/pre-tool-validator.py` | PreToolUse hook - blocks critical vulns |
| `hooks/post-tool-scanner.py` | PostToolUse hook - scans and logs |
| `reference/owasp-guide.md` | OWASP Top 10 quick reference |
| `reference/secure-patterns.md` | Secure coding patterns |

### security-guardian Commands

| Command | Action |
|---------|--------|
| `/security-guardian scan [path]` | Scan file/directory for vulnerabilities |
| `/security-guardian audit` | Full project security audit |
| `/security-guardian secrets` | Focused credential scan |
| `/security-guardian baas [provider]` | BaaS configuration audit |
| `/security-guardian status` | Show iteration tracking status |
| `/security-guardian report [format]` | Generate SARIF/markdown/JSON report |

### security-guardian Research Basis

| Source | Finding |
|--------|---------|
| arXiv:2506.11022 | +37.6% critical vulns after 5 AI iterations |
| Escape.tech 2025 | 2,000+ vulns in 5,600 vibe-coded apps |
| CVE-2025-54794/54795 | Claude Code path traversal & command injection |

---

## Components

| Name | Type | Location | Purpose |
|------|------|----------|---------|

---

## Key Functions

| Function | Location | Lines | What it does |
|----------|----------|-------|--------------|

---

## API Endpoints

| Method | Route | Handler | Auth required |
|--------|-------|---------|---------------|

---

## Database

### Tables
| Table | Key columns | Used by |
|-------|-------------|---------|

### Important queries
| Name | Location | What it does |
|------|----------|--------------|

---

## Data Flows

---

## External Dependencies

| Package | Version | Used for |
|---------|---------|----------|

---

## Environment Variables

| Variable | Required | Purpose |
|----------|----------|---------|

---

## Notes

*Anything else I've learned that doesn't fit above.*

---

## How I Use This

1. **Before claiming something exists:** `grep "name" .claude/docs/registry.md`
2. **After discovering something:** Add it here immediately
3. **Before implementing:** Check what's already here
4. **After implementing:** Update with new components/functions

**If I'm about to write code that calls a function not listed here, I STOP and verify it exists first.**
