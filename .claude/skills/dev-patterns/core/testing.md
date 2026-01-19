# Testing Principles (Language-Agnostic)

## Test Pyramid

```
        /\
       /  \         E2E Tests
      /    \        Few, slow, high confidence
     /------\
    /        \      Integration Tests
   /          \     Some, medium speed
  /------------\
 /              \   Unit Tests
/                \  Many, fast, isolated
```

### Distribution Guideline
- **Unit:** 70% - Fast, isolated, test logic
- **Integration:** 20% - Test component interactions
- **E2E:** 10% - Test critical user flows

---

## TDD Cycle (Universal)

```
1. RED:      Write a failing test
2. GREEN:    Write minimal code to pass
3. REFACTOR: Improve code, keep tests green
4. REPEAT
```

### Quando TDD e Appropriato
- Business logic critica
- Funzioni pure con I/O definiti
- Algoritmi complessi
- Bug fix (scrivi test che riproduce, poi fix)

### Quando TDD e Opzionale
- Prototipi e spike
- UI (preferire visual/snapshot tests)
- Integrazione API esterne
- Glue code semplice

---

## AAA Pattern (Arrange-Act-Assert)

```
test "user can add item to cart":
    # Arrange - Setup
    cart = new ShoppingCart()
    item = { id: "1", price: 9.99 }

    # Act - Execute
    cart.add(item)

    # Assert - Verify
    assert cart.items.length == 1
    assert cart.total == 9.99
```

### Variante: Given-When-Then (BDD)
```
given "an empty cart"
when "user adds an item"
then "cart contains one item"
```

---

## Test Naming Convention

### Pattern: should_[expected]_when_[condition]

```
should_return_empty_list_when_no_users_exist
should_throw_error_when_email_invalid
should_apply_discount_when_order_over_100
```

### Alternative Patterns
```
# Verb-based
returnsEmptyListWhenNoUsersExist

# Context-based (describe blocks)
describe "UserService"
  describe "findByEmail"
    it "returns null when user not found"
    it "returns user when email matches"
```

---

## Coverage Strategy

| Area | Target | Rationale |
|------|--------|-----------|
| Business Logic | 90%+ | Critico, testabile |
| API Handlers | 80%+ | Entry points |
| UI Components | 60%+ | Visual tests complementano |
| Config/Glue | 40%+ | Bassa complessita |

### Coverage Caveats
- 100% coverage != no bugs
- Coverage misura linee eseguite, non logica testata
- Punta a coverage significativo, non numeri alti

---

## Cosa Testare

### SI
- Edge cases (null, empty, max values)
- Error paths (exceptions, failures)
- Business rules
- Security boundaries
- State transitions
- Race conditions (se applicabile)

### NO
- Framework internals
- Third-party libraries
- Trivial getters/setters
- Implementation details
- Private methods (testa via public API)

---

## Test Doubles

### Tipi di Test Doubles

| Tipo | Scopo | Quando Usare |
|------|-------|--------------|
| **Dummy** | Riempie parametri non usati | Parametri obbligatori ma irrilevanti |
| **Stub** | Ritorna valori predefiniti | Controllare input al SUT |
| **Spy** | Registra chiamate | Verificare che metodo sia chiamato |
| **Mock** | Stub + verifiche | Verificare interazioni |
| **Fake** | Implementazione semplificata | In-memory DB, fake server |

### Mock External, Test Internal

```
# GOOD: Mock external dependency
mock(stripe_api).charge.returns({ success: true })

# BAD: Mock internal logic
mock(calculate_tax)  # Test this directly instead!
```

### When to Mock
- External services (APIs, DBs)
- Time-dependent code
- Random number generators
- File system (sometimes)

### When NOT to Mock
- Internal business logic
- Value objects
- Pure functions
- Anything you own and can test directly

---

## Test Isolation

Ogni test deve:
- Essere indipendente dagli altri
- Non dipendere dall'ordine di esecuzione
- Pulire il proprio stato (setup/teardown)
- Poter girare in parallelo

### Database Testing
- Ogni test ha il suo setup
- Transaction rollback after test
- O fresh database per ogni test

---

## Test Organization

### Per Feature/Module
```
src/
  users/
    user.service.ts
    user.service.test.ts    # co-located
```

### Separate Test Directory
```
src/
  users/
    user.service.ts
tests/
  users/
    user.service.test.ts
```

### Test Types Separation
```
tests/
  unit/
  integration/
  e2e/
```

---

## Flaky Tests

### Cause Comuni
- Timing/race conditions
- External dependencies
- Shared state
- Order dependency
- Time-dependent logic

### Soluzioni
- Mock time instead of using real time
- Use deterministic test data
- Isolate tests properly
- Retry with investigation (not blind retry)

---

## Integration Testing

### Cosa Testare
- Database queries funzionano
- API endpoints rispondono correttamente
- Services comunicano
- Authentication/Authorization funziona

### Setup
- Test containers (Docker)
- In-memory databases
- Mock servers per external APIs

---

## E2E Testing

### Cosa Testare
- Critical user journeys
- Happy paths principali
- Main error scenarios

### Best Practices
- Keep them few and focused
- Use stable selectors (data-testid)
- Handle async properly
- Clean state between tests

---

## Test Data

### Factories/Builders
```
# Instead of:
user = User(name="test", email="test@test.com", age=25, ...)

# Use factory:
user = UserFactory.create()
user = UserFactory.create(email="custom@email.com")
```

### Fixtures
- Predefined test data
- Good for complex scenarios
- Risk: can become stale

### Random Data
- Good for finding edge cases
- Property-based testing
- Must be reproducible (seeded)

---

## Performance Testing Basics

### Types
- **Load testing**: Normal expected load
- **Stress testing**: Beyond normal capacity
- **Spike testing**: Sudden load increase
- **Soak testing**: Extended period

### Metrics to Measure
- Response time (p50, p95, p99)
- Throughput (requests/second)
- Error rate
- Resource usage (CPU, memory)

---

## Testing Checklist

### Before Committing
- [ ] All tests pass locally
- [ ] New code has tests
- [ ] Bug fix has regression test
- [ ] No commented-out tests
- [ ] No skipped tests without reason

### Code Review
- [ ] Tests are readable
- [ ] Tests cover edge cases
- [ ] Mocks are appropriate
- [ ] No test interdependencies
