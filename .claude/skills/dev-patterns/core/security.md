# Security Checklist (Language-Agnostic)

## Input Validation

### Principles
- **Whitelist over Blacklist**: Definisci cosa e permesso, non cosa e vietato
- **Validate at Boundaries**: Input utente, API calls, file uploads
- **Fail Closed**: Se la validazione fallisce, rifiuta

### Checklist
- [ ] Tutti gli input utente validati
- [ ] Lunghezza massima definita per stringhe
- [ ] Tipi verificati (numero e numero, non stringa)
- [ ] Range verificati per valori numerici
- [ ] Format verificati (email, URL, date)
- [ ] File upload: tipo, dimensione, estensione
- [ ] No path traversal (../)
- [ ] Encoding corretto (UTF-8)

### Validation Examples
```
# String
- Max length: 255 chars
- No control characters
- Trim whitespace

# Email
- Max length: 254 chars
- Valid format (RFC 5322)
- Domain exists (optional)

# URL
- Valid scheme (https only?)
- No internal IPs (SSRF prevention)
- Whitelist allowed domains if possible

# Numbers
- Within expected range
- No negative where inappropriate
- Handle overflow
```

---

## Authentication & Authorization

### Authentication (Chi sei?)
- [ ] Password hashate con algoritmo forte (bcrypt, argon2, scrypt)
- [ ] Token con scadenza ragionevole
- [ ] Rate limiting su login (prevent brute force)
- [ ] No credenziali in URL (visible in logs!)
- [ ] Session invalidation on logout
- [ ] MFA per operazioni sensibili
- [ ] Account lockout after failed attempts

### Password Requirements
- Minimum 12 characters
- No maximum length (allow passphrases)
- Check against breached password lists
- No complexity rules (they don't help)

### Authorization (Cosa puoi fare?)
- [ ] Check autorizzazione su OGNI richiesta
- [ ] Principle of Least Privilege
- [ ] No client-side authorization checks as only defense
- [ ] RBAC o ABAC implementato correttamente
- [ ] Verify resource ownership (can user X access resource Y?)
- [ ] Re-verify on sensitive operations

### Authorization Patterns
```
# RBAC (Role-Based)
user.hasRole("admin")

# ABAC (Attribute-Based)
user.canAccess(resource, action)

# Resource-Based
resource.owner == currentUser
```

---

## Data Protection

### In Transit
- [ ] HTTPS everywhere (no HTTP)
- [ ] TLS 1.2+ only (deprecate 1.0, 1.1)
- [ ] HSTS enabled (Strict-Transport-Security)
- [ ] Certificate pinning (mobile apps)
- [ ] No mixed content

### At Rest
- [ ] Sensitive data encrypted (AES-256)
- [ ] Key management appropriato (not in code!)
- [ ] Backup crittografati
- [ ] Secure deletion when needed

### In Memory
- [ ] Clear sensitive data after use
- [ ] Don't log sensitive data
- [ ] Careful with debug output

### In Logs
- [ ] No passwords in logs
- [ ] No tokens in logs
- [ ] No PII in logs (or masked)
- [ ] No stack traces in production logs
- [ ] No credit card numbers
- [ ] Mask sensitive fields

---

## Injection Prevention

### SQL Injection
- [ ] Parameterized queries ALWAYS
- [ ] No string concatenation in queries
- [ ] ORM usato correttamente
- [ ] Escape user input if raw queries needed

```
# BAD
query = "SELECT * FROM users WHERE id = " + userId

# GOOD
query = "SELECT * FROM users WHERE id = ?"
execute(query, [userId])
```

### Command Injection
- [ ] No shell execution con input utente
- [ ] Se necessario, whitelist di comandi
- [ ] Use language APIs instead of shell
- [ ] Escape appropriato if unavoidable

```
# BAD
os.system("convert " + filename)

# GOOD
subprocess.run(["convert", filename], shell=False)
```

### XSS (Cross-Site Scripting)
- [ ] Output encoding (HTML entities)
- [ ] Content Security Policy header
- [ ] HttpOnly cookies
- [ ] No innerHTML con dati utente
- [ ] Sanitize HTML if allowing rich text

```
# BAD
element.innerHTML = userInput

# GOOD
element.textContent = userInput
# or
element.innerHTML = sanitize(userInput)
```

### Path Traversal
- [ ] Validate file paths
- [ ] Use canonical paths
- [ ] Whitelist allowed directories
- [ ] Don't trust user-provided filenames

```
# BAD
file = open("/uploads/" + userFilename)

# GOOD
safe_name = os.path.basename(userFilename)
file = open("/uploads/" + safe_name)
```

---

## CSRF Protection

- [ ] CSRF tokens for state-changing operations
- [ ] SameSite cookie attribute
- [ ] Verify Origin/Referer headers
- [ ] Double-submit cookie pattern

---

## Session Security

- [ ] Regenerate session ID after login
- [ ] Session timeout (idle and absolute)
- [ ] Secure session storage
- [ ] Session cookies: Secure, HttpOnly, SameSite

---

## Secrets Management

### DO
- [ ] Secrets in environment variables
- [ ] Secrets in vault (production)
- [ ] Different secrets per environment
- [ ] Rotate secrets periodically
- [ ] Audit access to secrets

### DON'T
- [ ] No hardcoded secrets
- [ ] No secrets in git
- [ ] No secrets in logs
- [ ] No secrets in error messages
- [ ] No secrets in URLs
- [ ] No secrets in client-side code

### Secret Rotation
- API keys: quarterly
- Database passwords: quarterly
- JWT signing keys: annually
- After any suspected breach: immediately

---

## Error Handling Security

### DO
- Messaggi generici per utenti
- Log dettagliati server-side
- Error codes consistenti
- Proper HTTP status codes

### DON'T
- Stack traces all'utente
- Dettagli di implementazione
- Path del filesystem
- Query SQL negli errori
- Database connection strings

### Example
```
# BAD (exposes internals)
"Error: ENOENT /var/app/users/123.json"

# GOOD (generic message)
"User not found"
```

---

## OWASP Top 10 Quick Reference

| # | Risk | Mitigation |
|---|------|------------|
| 1 | Broken Access Control | AuthZ checks everywhere |
| 2 | Cryptographic Failures | Use standard libraries |
| 3 | Injection | Parameterized queries |
| 4 | Insecure Design | Threat modeling |
| 5 | Security Misconfiguration | Hardening, updates |
| 6 | Vulnerable Components | Dependency scanning |
| 7 | Auth Failures | MFA, rate limiting |
| 8 | Data Integrity | Signatures, checksums |
| 9 | Logging Failures | Centralized logging |
| 10 | SSRF | Whitelist URLs |

---

## HTTP Security Headers

```
# Essential
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Strict-Transport-Security: max-age=31536000; includeSubDomains

# Additional
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), camera=(), microphone=()
```

---

## Dependency Security

- [ ] Regular dependency updates
- [ ] Automated vulnerability scanning
- [ ] Lock file committed
- [ ] Review new dependencies before adding
- [ ] Minimize dependencies

### Tools (examples)
- npm audit / yarn audit (Node.js)
- pip-audit (Python)
- cargo audit (Rust)
- Dependabot / Snyk (multi-language)

---

## Security Testing

### SAST (Static Analysis)
- Analyze code without running
- Find patterns that indicate vulnerabilities
- Run in CI/CD

### DAST (Dynamic Analysis)
- Test running application
- Find runtime vulnerabilities
- Penetration testing

### Security Review Checklist
- [ ] Input validation complete
- [ ] Auth/AuthZ implemented
- [ ] Data encrypted appropriately
- [ ] Logging doesn't expose secrets
- [ ] Dependencies are secure
- [ ] Headers configured correctly

---

## Incident Response Preparation

### Before Incident
- [ ] Logging enabled and centralized
- [ ] Alerts configured
- [ ] Contact list ready
- [ ] Runbooks prepared
- [ ] Backup and restore tested

### During Incident
1. Contain (limit damage)
2. Investigate (understand scope)
3. Remediate (fix vulnerability)
4. Communicate (stakeholders)

### After Incident
- [ ] Post-mortem conducted
- [ ] Lessons documented
- [ ] Preventive measures implemented
- [ ] Team trained on findings
