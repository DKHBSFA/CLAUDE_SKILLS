# Feature: Security Guardian Skill

**Status:** COMPLETE
**Created:** 2026-01-17 10:30 UTC
**Approved:** 2026-01-17 11:00 UTC
**Completed:** 2026-01-17 12:30 UTC

---

## 1. Overview

**What?** Skill Claude Code per analisi di sicurezza specifica per codice AI-generated, con focus su pattern di vulnerabilità emergenti dal "vibe coding".

**Why?** Le ricerche verificate (arXiv:2506.11022, Escape.tech) dimostrano:
- +37.6% vulnerabilità critiche dopo 5 iterazioni AI
- 2,000+ vulnerabilità in app vibe-coded (5,600 app analizzate)
- 10.3% app con misconfigurazioni Supabase critiche
- CVE-2025-54794/54795 dimostrano vulnerabilità in Claude Code stesso

**For whom?** Sviluppatori che usano Claude Code per generare codice, team che adottano vibe coding, progetti con backend BaaS (Supabase, Firebase, etc.)

**Success metric:**
- Rilevamento ≥80% pattern OWASP Top 10 in codice generato
- Zero false positive su credential exposure in bundle
- Tempo di scan <500ms per file

---

## 2. Verifica Fonti (Completata)

### ✅ Fonti Confermate

| Claim | Fonte | Status |
|-------|-------|--------|
| 37.6% vulnerabilità dopo 5 iterazioni | [arXiv:2506.11022v2](https://arxiv.org/abs/2506.11022) - IEEE ISTAS 2025 | **VERIFICATO** |
| 2,000+ vulnerabilità vibe-coded | [Escape.tech](https://escape.tech/blog/methodology-how-we-discovered-vulnerabilities-apps-built-with-vibe-coding/) | **VERIFICATO** |
| CVE-2025-54794 (path traversal) | [Cymulate](https://cymulate.com/blog/cve-2025-547954-54795-claude-inverseprompt/) | **VERIFICATO** |
| CVE-2025-54795 (command injection) | [Miggo](https://www.miggo.io/vulnerability-database/cve/CVE-2025-54795) | **VERIFICATO** |
| 5,600 app analizzate | [Escape.tech State of Security](https://escape.tech/state-of-security-of-vibe-coded-apps) | **VERIFICATO** |

### Dati Chiave dal Paper arXiv:2506.11022

- **Metodologia**: 400 sample, 40 round iterazioni, 4 strategie di prompting
- **Finding critico**: Security-focused prompts creano 21.1% errori crittografici (paradosso)
- **Correlazione**: r=0.64 tra complessità ciclomatica e vulnerabilità
- **Raccomandazione**: Review obbligatoria dopo 3-5 iterazioni

---

## 3. Scope MVP vs Nice-to-Have

### MVP (Fase 1) - Essenziale

| Modulo | Funzionalità | Priorità |
|--------|--------------|----------|
| **Pattern Scanner** | Regex-based detection OWASP Top 10 | CRITICO |
| **Secret Detector** | Credenziali in codice/bundle | CRITICO |
| **BaaS Auditor** | Supabase/Firebase config check | ALTO |
| **Iteration Tracker** | Contatore iterazioni AI per file | ALTO |
| **Hook Integration** | PreToolUse/PostToolUse hooks | CRITICO |

### Fase 2 - Importante

| Modulo | Funzionalità | Priorità |
|--------|--------------|----------|
| **Dependency Scanner** | CVE lookup per package.json/requirements.txt | MEDIO |
| **Logic Analyzer** | Rilevamento boolean inversion | MEDIO |
| **Complexity Monitor** | Delta complessità ciclomatica | MEDIO |
| **SARIF Reporter** | Output standard per GitHub Security | MEDIO |

### Nice-to-Have (Fase 3+)

| Modulo | Funzionalità | Priorità |
|--------|--------------|----------|
| **AST Deep Analysis** | Parsing completo per taint analysis | BASSO |
| **Multi-BaaS Support** | AWS Amplify, PocketBase, etc. | BASSO |
| **Compliance Mapping** | ISO 27001, SOC 2 report | BASSO |
| **Dashboard Web** | Visualizzazione trend | BASSO |

---

## 4. Technical Approach

### 4.1 Architettura Skill

```
.claude/skills/security-guardian/
├── SKILL.md                    # Definizione skill (entry point)
├── patterns/
│   ├── owasp-top-10.json      # Pattern detection rules
│   ├── secrets.json           # Credential patterns
│   └── baas-misconfig.json    # BaaS-specific patterns
├── scripts/
│   ├── scanner.py             # Core scanning engine
│   ├── secret-detector.py     # Secret detection
│   ├── baas-auditor.py        # BaaS configuration audit
│   └── iteration-tracker.py   # AI iteration tracking
├── hooks/
│   ├── pre-tool-validator.py  # PreToolUse hook
│   └── post-tool-scanner.py   # PostToolUse hook
├── reference/
│   ├── owasp-guide.md         # OWASP Top 10 reference
│   ├── secure-patterns.md     # Secure coding examples
│   └── cwe-mapping.md         # CWE identifier reference
└── .security-guardian/
    └── state.json             # Iteration tracking state
```

### 4.2 Pattern Design

**Differenza chiave da analisi originale**:
- ❌ NON usiamo iteration limit rigido (blocco dopo 3)
- ✅ Usiamo warning progressivo con severity crescente
- ❌ NON metadata injection nel codice sorgente
- ✅ File separato `.security-guardian/state.json`

### 4.3 Hook Strategy

| Hook Event | Trigger | Azione |
|------------|---------|--------|
| `PreToolUse` | Write/Edit tools | Valida codice PRIMA della scrittura |
| `PostToolUse` | Write/Edit completati | Scan post-scrittura, aggiorna iteration count |
| `UserPromptSubmit` | Ogni prompt utente | Log per audit trail |

### 4.4 Exit Code Strategy (Hook)

| Exit Code | Significato | Azione Claude |
|-----------|-------------|---------------|
| `0` | Validazione passata | Procede normalmente |
| `1` | Errore hook (non-blocking) | Warning, procede |
| `2` | Violazione sicurezza | **BLOCCA**, mostra errore |

---

## 5. Files to Create

| File | Action | Purpose |
|------|--------|---------|
| `.claude/skills/security-guardian/SKILL.md` | Create | Skill definition, commands, workflow |
| `.claude/skills/security-guardian/patterns/owasp-top-10.json` | Create | 50+ security patterns |
| `.claude/skills/security-guardian/patterns/secrets.json` | Create | 30+ credential patterns |
| `.claude/skills/security-guardian/patterns/baas-misconfig.json` | Create | Supabase/Firebase patterns |
| `.claude/skills/security-guardian/scripts/scanner.py` | Create | Core scanning engine |
| `.claude/skills/security-guardian/scripts/secret-detector.py` | Create | Secret detection logic |
| `.claude/skills/security-guardian/scripts/baas-auditor.py` | Create | BaaS config analysis |
| `.claude/skills/security-guardian/scripts/iteration-tracker.py` | Create | AI iteration tracking |
| `.claude/skills/security-guardian/hooks/pre-tool-validator.py` | Create | PreToolUse validation hook |
| `.claude/skills/security-guardian/hooks/post-tool-scanner.py` | Create | PostToolUse scanning hook |
| `.claude/skills/security-guardian/reference/owasp-guide.md` | Create | OWASP reference doc |
| `.claude/skills/security-guardian/reference/secure-patterns.md` | Create | Secure coding examples |
| `docs/registry.md` | Modify | Add security-guardian skill entry |
| `docs/decisions.md` | Modify | Document architectural choices |

---

## 6. SKILL.md Design

### Commands

| Command | Purpose | Trigger |
|---------|---------|---------|
| `/security-guardian scan [file\|dir]` | Scan manuale di file/directory | User-invoked |
| `/security-guardian audit` | Full project security audit | User-invoked |
| `/security-guardian secrets` | Scan solo per credenziali esposte | User-invoked |
| `/security-guardian baas` | Audit configurazione BaaS | User-invoked |
| `/security-guardian status` | Mostra iteration count per file | User-invoked |
| `/security-guardian report` | Genera report SARIF | User-invoked |

### Enforcement Rules

| Rule | Severity | Action |
|------|----------|--------|
| Hardcoded credentials | CRITICAL | BLOCK |
| SQL injection pattern | CRITICAL | BLOCK |
| Command injection | CRITICAL | BLOCK |
| XSS vulnerability | HIGH | BLOCK |
| Insecure crypto (MD5/SHA1) | HIGH | WARN |
| RLS disabled (Supabase) | CRITICAL | BLOCK |
| Exposed service key | CRITICAL | BLOCK |
| Missing input validation | MEDIUM | WARN |
| Iteration count > 5 | MEDIUM | WARN (progressivo) |
| Complexity delta > 30% | LOW | INFO |

---

## 7. Pattern Database (MVP)

### 7.1 OWASP Top 10 Patterns

```json
{
  "A01_broken_access_control": [
    {"id": "BAC-001", "pattern": "(?i)role\\s*[=!]=\\s*['\"]admin['\"].*\\|\\|", "severity": "HIGH", "cwe": "CWE-284"},
    {"id": "BAC-002", "pattern": "(?i)\\.skip\\s*\\(.*user", "severity": "HIGH", "cwe": "CWE-639"}
  ],
  "A02_cryptographic_failures": [
    {"id": "CF-001", "pattern": "(?i)md5|sha1(?!-)", "severity": "HIGH", "cwe": "CWE-328"},
    {"id": "CF-002", "pattern": "(?i)createCipher\\(|DES|RC4", "severity": "CRITICAL", "cwe": "CWE-327"}
  ],
  "A03_injection": [
    {"id": "INJ-001", "pattern": "(?i)execute\\s*\\(\\s*[f'\"]", "severity": "CRITICAL", "cwe": "CWE-89"},
    {"id": "INJ-002", "pattern": "(?i)\\$\\{.*\\}.*query|query.*\\$\\{", "severity": "CRITICAL", "cwe": "CWE-89"},
    {"id": "INJ-003", "pattern": "(?i)eval\\s*\\(|exec\\s*\\(|os\\.system\\(", "severity": "CRITICAL", "cwe": "CWE-78"}
  ],
  "A07_xss": [
    {"id": "XSS-001", "pattern": "(?i)innerHTML\\s*=|document\\.write\\(", "severity": "HIGH", "cwe": "CWE-79"},
    {"id": "XSS-002", "pattern": "(?i)dangerouslySetInnerHTML", "severity": "HIGH", "cwe": "CWE-79"}
  ]
}
```

### 7.2 Secret Patterns

```json
{
  "api_keys": [
    {"id": "SEC-001", "pattern": "(?i)(api[_-]?key|apikey)\\s*[:=]\\s*['\"][\\w-]{20,}['\"]", "severity": "CRITICAL"},
    {"id": "SEC-002", "pattern": "sk_live_[a-zA-Z0-9]{24,}", "severity": "CRITICAL", "provider": "Stripe"},
    {"id": "SEC-003", "pattern": "ghp_[a-zA-Z0-9]{36}", "severity": "CRITICAL", "provider": "GitHub"},
    {"id": "SEC-004", "pattern": "xoxb-[0-9]{10,}-[a-zA-Z0-9]{24}", "severity": "CRITICAL", "provider": "Slack"}
  ],
  "baas_keys": [
    {"id": "BAAS-001", "pattern": "(?i)supabase.*service_role", "severity": "CRITICAL", "provider": "Supabase"},
    {"id": "BAAS-002", "pattern": "(?i)NEXT_PUBLIC_SUPABASE_SERVICE", "severity": "CRITICAL", "provider": "Supabase"},
    {"id": "BAAS-003", "pattern": "(?i)firebase.*private_key", "severity": "CRITICAL", "provider": "Firebase"}
  ],
  "jwt_tokens": [
    {"id": "JWT-001", "pattern": "eyJ[A-Za-z0-9_-]*\\.[A-Za-z0-9_-]*\\.[A-Za-z0-9_-]*", "severity": "HIGH"}
  ]
}
```

### 7.3 BaaS Misconfig Patterns (Supabase Focus)

```json
{
  "supabase": [
    {"id": "SUP-001", "pattern": "(?i)\\.rpc\\(['\"].*['\"]\\)(?!.*auth)", "severity": "MEDIUM", "issue": "RPC without auth check"},
    {"id": "SUP-002", "pattern": "(?i)supabase\\.from\\(.*\\)\\.select\\(.*\\*.*\\)", "severity": "MEDIUM", "issue": "SELECT * exposes all columns"},
    {"id": "SUP-003", "pattern": "(?i)service_role.*anon|anon.*service_role", "severity": "CRITICAL", "issue": "Key confusion"},
    {"id": "SUP-004", "pattern": "(?i)supabaseUrl.*supabaseKey.*createClient", "severity": "HIGH", "issue": "Check key type in client bundle"}
  ],
  "firebase": [
    {"id": "FB-001", "pattern": "(?i)rules_version.*allow\\s+read,\\s*write:\\s*if\\s+true", "severity": "CRITICAL", "issue": "Open rules"},
    {"id": "FB-002", "pattern": "(?i)firebase.*private_key_id", "severity": "CRITICAL", "issue": "Service account in client"}
  ]
}
```

---

## 8. Iteration Tracking Design

### State File: `.security-guardian/state.json`

```json
{
  "version": "1.0.0",
  "session_id": "${CLAUDE_SESSION_ID}",
  "files": {
    "src/auth/login.ts": {
      "iterations": 4,
      "first_seen": "2026-01-17T10:00:00Z",
      "last_modified": "2026-01-17T10:45:00Z",
      "complexity_baseline": 12,
      "complexity_current": 18,
      "complexity_delta_percent": 50,
      "vulnerabilities_found": ["INJ-001", "SEC-002"],
      "warnings_shown": 2
    }
  },
  "session_stats": {
    "total_scans": 45,
    "blocked_operations": 3,
    "warnings_issued": 12
  }
}
```

### Warning Escalation

| Iterations | Severity | Message |
|------------|----------|---------|
| 1-3 | INFO | "Iteration {n}/5 - Consider review if making significant changes" |
| 4-5 | WARNING | "⚠️ Iteration {n}/5 - Research shows 37.6% more vulnerabilities after 5 iterations. Human review recommended." |
| 6+ | HIGH | "🔴 Iteration {n} - High risk zone. arXiv:2506.11022 shows exponential vulnerability growth. STRONGLY recommend code review before continuing." |

**Nota**: Non blocchiamo MAI basandoci solo su iteration count. È un warning, non un blocco.

---

## 9. Test Specification

### Unit Tests

| ID | What I'm testing | Input | Expected | Priority |
|----|------------------|-------|----------|----------|
| UT-01 | SQL injection detection | `execute(f"SELECT * FROM {table}")` | Match INJ-001 | High |
| UT-02 | Secret detection (Stripe) | `sk_live_abc123...` | Match SEC-002 | High |
| UT-03 | XSS detection | `innerHTML = userInput` | Match XSS-001 | High |
| UT-04 | False positive avoidance | `// sk_live_example_not_real` | No match (comment) | High |
| UT-05 | Iteration increment | File edited twice | iterations = 2 | Medium |

### Integration Tests

| ID | Flow | Components | Expected | Priority |
|----|------|------------|----------|----------|
| IT-01 | PreToolUse → Block | Hook + Scanner | Exit 2, operation blocked | High |
| IT-02 | Full scan → Report | Scanner + All patterns | SARIF output | Medium |
| IT-03 | BaaS audit → Findings | BaaS auditor + Supabase | List misconfigs | High |

### Security Tests

| ID | Threat | Attack | Expected defense |
|----|--------|--------|------------------|
| ST-01 | Hook bypass | Malformed JSON input | Graceful failure, exit 1 |
| ST-02 | Path traversal | `../../etc/passwd` in scan path | Reject, stay in project |
| ST-03 | Regex DoS | Evil regex input | Timeout protection |

---

## 10. Architectural Decisions

### Decision 1: Warning vs Blocking for Iterations

**Decision**: Warning progressivo, mai blocco basato solo su iteration count
**Why**:
- L'analisi originale proponeva blocco rigido dopo 3 iterazioni
- Questo viola il principio di developer agency
- Il paper arXiv mostra correlazione, non causalità diretta
**Affects**: Iteration tracker emette warning, non blocchi

### Decision 2: File-based State vs Code Injection

**Decision**: State in `.security-guardian/state.json`, non nei commenti del codice
**Why**:
- L'analisi proponeva `// ai-guardian: iterations=2` nei file
- Questo inquina il codice sorgente
- Problemi con formattatori, linter, merge conflicts
**Affects**: Tracking completamente separato dal codice

### Decision 3: BaaS-Agnostic vs Supabase-Specific

**Decision**: Architettura plugin per BaaS multipli, MVP con Supabase
**Why**:
- L'analisi era troppo Supabase-centrica
- Firebase, AWS Amplify, PocketBase sono altrettanto usati
- Pattern database modulare permette estensione
**Affects**: Pattern files separati per provider

### Decision 4: Complementare, Non Duplicare

**Decision**: Non reimplementare safety checks già in Claude Code
**Why**:
- Claude Code ha già protezioni built-in (sandbox, permission system)
- La skill deve aggiungere valore, non ridondanza
- Anthropic non espone Safety API standalone
**Affects**: Focus su pattern AI-specific che Claude non cattura nativamente

---

## 11. Dipendenze

### Runtime

- Python 3.8+ (per script hooks)
- `re` module (regex, stdlib)
- `json` module (pattern loading, stdlib)
- `pathlib` module (path handling, stdlib)

### Optional (Fase 2)

- `semgrep` - AST-based analysis
- `bandit` - Python security linter
- `eslint-plugin-security` - JS security rules

### Zero External Dependencies per MVP

La skill MVP usa solo Python stdlib per massima portabilità.

---

## 12. Rischi e Mitigazioni

| Rischio | Probabilità | Impatto | Mitigazione |
|---------|-------------|---------|-------------|
| False positives eccessivi | Media | Alto | Tuning pattern, context awareness |
| Performance degradation | Bassa | Medio | Timeout hooks (10s), async scan |
| Hook bypass | Bassa | Alto | Multiple hook points, pre+post |
| Pattern obsolescence | Media | Medio | Pattern database aggiornabile |
| Regex DoS | Bassa | Medio | Timeout per regex, pattern review |

---

## 13. Success Criteria per Fase

### MVP (Fase 1)

- [ ] Skill caricabile con `/security-guardian`
- [ ] Scan manuale funzionante
- [ ] Detection rate ≥80% su OWASP Top 10 test suite
- [ ] Zero false positive su secret patterns validati
- [ ] Hooks funzionanti (PreToolUse, PostToolUse)
- [ ] Iteration tracking operativo
- [ ] Documentazione completa

### Fase 2

- [ ] Dependency scanning (CVE lookup)
- [ ] SARIF output per GitHub integration
- [ ] Logic analyzer per boolean inversion
- [ ] Multi-BaaS support (Firebase)

---

## 14. Implementation Notes

*Da compilare durante l'implementazione*

---

## 15. Open Questions

1. **Complexity calculation**: Usare tool esterno (radon, escomplex) o implementazione semplificata?
   - **Proposta**: MVP con line count + nesting depth, Fase 2 con tool dedicato

2. **Pattern update mechanism**: Come aggiornare pattern database?
   - **Proposta**: File JSON versionati, update manuale per MVP

3. **Cross-file analysis**: Scan singolo file o progetto intero?
   - **Proposta**: MVP file singolo, Fase 2 project-wide

---

**Awaiting PROCEED to begin implementation**
