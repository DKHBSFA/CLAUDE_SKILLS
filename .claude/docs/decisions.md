# Architectural Decisions

**Why things are the way they are.**

When I make a choice that affects future work, I record it here. This prevents me from proposing contradictory approaches later.

---

## Format

```markdown
### [Short title]
**Date:** YYYY-MM-DD
**Decision:** What was decided
**Why:** Why this over alternatives
**Affects:** What this impacts going forward
```

---

## Decisions

<!-- New entries go here, newest first -->

### Security Guardian: Warning vs Blocking for AI Iterations
**Date:** 2026-01-17
**Decision:** Use progressive warnings instead of hard blocking based on iteration count
**Why:** Original analysis proposed blocking after 3 iterations. This violates developer agency and the arXiv research shows correlation, not causation. Blocking would be too disruptive.
**Affects:** Iteration tracker emits warnings at 4+ iterations, strong warnings at 6+, but never blocks solely based on count

### Security Guardian: Separate State File vs Code Comments
**Date:** 2026-01-17
**Decision:** Store iteration tracking in `.security-guardian/state.json`, not in code comments
**Why:** Original analysis proposed injecting `// ai-guardian: iterations=2` into source files. This pollutes code, causes issues with formatters/linters, and creates merge conflicts.
**Affects:** All iteration tracking is in separate JSON files, not embedded in source

### Security Guardian: BaaS-Agnostic Architecture
**Date:** 2026-01-17
**Decision:** Design pattern database to support multiple BaaS providers, not just Supabase
**Why:** Original analysis was too Supabase-centric. Firebase, AWS Amplify, PocketBase are equally common. Plugin architecture allows extension.
**Affects:** `baas-misconfig.json` has separate sections per provider, `baas-auditor.py` auto-detects provider

### Security Guardian: Complement, Not Duplicate Claude's Safety
**Date:** 2026-01-17
**Decision:** Focus on AI-specific patterns that Claude Code doesn't catch natively
**Why:** Claude Code has built-in safety features (sandbox, permissions). Skill should add value, not redundancy. Anthropic doesn't expose standalone Safety APIs.
**Affects:** Patterns focus on vibe-coding-specific issues: iteration degradation, BaaS misconfig, logic inversion

### Security Guardian: Python-Only with Zero External Dependencies
**Date:** 2026-01-17
**Decision:** MVP uses only Python standard library (re, json, pathlib)
**Why:** Maximum portability across systems. No need for pip install. Users can run immediately.
**Affects:** No semgrep, bandit, or other external tools in MVP. Phase 2 may add optional integrations.

---

*When I'm about to make an architectural choice, I check here first to stay consistent.*
