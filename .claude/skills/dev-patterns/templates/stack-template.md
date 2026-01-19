# Stack Patterns: [STACK_NAME]

**Generated:** [DATE]
**Stack:** [LANGUAGE] + [FRAMEWORK] + [DATABASE]

---

## Language Idioms

### [LANGUAGE] Best Practices

[Inserire idiomi specifici del linguaggio]

- Naming conventions (snake_case, camelCase, PascalCase)
- File organization
- Import patterns
- Common standard library usage

### Type System (se applicabile)

[Pattern per tipi, interfacce, generics]

```[language]
# Type definition patterns
# Interface usage
# Generic patterns
```

---

## Framework Patterns

### [FRAMEWORK] Project Structure

```
project/
├── src/
│   ├── components/     # [description]
│   ├── services/       # [description]
│   ├── utils/          # [description]
│   └── types/          # [description]
├── tests/
│   ├── unit/
│   └── integration/
├── config/
└── public/
```

### [FRAMEWORK] Component/Module Pattern

```[language]
// Canonical component/module structure
// Imports
// Types/interfaces
// Main implementation
// Exports
```

### [FRAMEWORK] State Management

[Pattern per gestione stato specifico del framework]

```[language]
// State management example
// Store creation
// Actions/mutations
// Selectors/getters
```

### [FRAMEWORK] Routing

[Pattern per routing specifico del framework]

```[language]
// Route definition
// Dynamic routes
// Protected routes
// Navigation
```

### [FRAMEWORK] Data Fetching

```[language]
// Server-side fetching
// Client-side fetching
// Caching patterns
// Error handling
```

---

## Database Integration

### [DATABASE] Connection Pattern

```[language]
// Database client initialization
// Connection pooling
// Environment-based config
```

### [DATABASE] Query Pattern

```[language]
// Basic CRUD operations
// Parameterized queries
// Transactions
```

### [DATABASE] Error Handling

```[language]
// Connection errors
// Query errors
// Constraint violations
// Retry logic
```

### [DATABASE] Migrations

```[language]
// Migration file structure
// Up/down migrations
// Seeding
```

---

## Testing

### Test Framework: [TESTING_FRAMEWORK]

```[language]
// Test file structure
// Describe/it blocks
// Setup/teardown
// Assertions
```

### Unit Test Example

```[language]
// Unit test for pure function
// Arrange-Act-Assert pattern
```

### Integration Test Example

```[language]
// Integration test for service
// Database mocking
// API mocking
```

### Mocking [DATABASE/API]

```[language]
// Mock setup
// Mock implementation
// Mock verification
```

---

## Common CLI Commands

| Action | Command |
|--------|---------|
| Install dependencies | [command] |
| Run development | [command] |
| Run tests | [command] |
| Run single test | [command] |
| Build production | [command] |
| Lint | [command] |
| Type check | [command] |
| Format code | [command] |
| Generate types | [command] |
| Database migrate | [command] |

---

## Environment Configuration

### Required Variables
```
DATABASE_URL=
API_KEY=
NODE_ENV=
```

### Optional Variables
```
LOG_LEVEL=
CACHE_TTL=
```

### .env.example
```
# Copy to .env.local and fill values
DATABASE_URL=postgresql://user:pass@localhost:5432/db
API_KEY=your-api-key
```

---

## Common Gotchas

### 1. [GOTCHA_TITLE]

**Problema:**
```[language]
// Code that causes the problem
```

**Sintomo:**
[Error message or unexpected behavior]

**Soluzione:**
```[language]
// Correct code
```

**Spiegazione:**
[Why this happens and how the fix works]

### 2. [GOTCHA_TITLE]

**Problema:**
```[language]
// Problematic code
```

**Soluzione:**
```[language]
// Fixed code
```

### 3. [GOTCHA_TITLE]

[Repeat pattern]

---

## Performance Tips

### [AREA] Optimization

```[language]
// Before (slow)
// After (optimized)
```

### Common Performance Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| N+1 queries | Slow list pages | Eager loading |
| Missing indexes | Slow filters | Add indexes |
| Large bundles | Slow load time | Code splitting |
| Memory leaks | Growing memory | Cleanup subscriptions |

---

## Security Considerations

### [FRAMEWORK]-Specific Security

- [ ] [Security check 1]
- [ ] [Security check 2]
- [ ] [Security check 3]

### Common Vulnerabilities

| Risk | Prevention |
|------|------------|
| XSS | [Framework-specific solution] |
| CSRF | [Framework-specific solution] |
| SQL Injection | [Framework-specific solution] |

---

## Debugging

### Development Tools
- [Tool 1]: [What it's for]
- [Tool 2]: [What it's for]

### Common Debug Commands

```bash
# Debug mode
[command]

# Verbose logging
[command]

# Inspect state
[command]
```

### Log Levels
```[language]
// How to configure logging
// Log level hierarchy
```

---

## Deployment

### Build Command
```bash
[build command]
```

### Build Output
```
dist/
├── [output files]
└── [description]
```

### Environment Variables for Production
```
NODE_ENV=production
[other prod vars]
```

---

## Resources

- [Official Documentation](url)
- [Best Practices Guide](url)
- [Community Resources](url)
- [Example Projects](url)

---

## Version Compatibility

| Dependency | Version | Notes |
|------------|---------|-------|
| [LANGUAGE] | X.Y.Z | [Compatibility notes] |
| [FRAMEWORK] | X.Y.Z | [Breaking changes] |
| [DATABASE] | X.Y.Z | [Feature availability] |
