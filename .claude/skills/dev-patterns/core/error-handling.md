# Error Handling Principles (Language-Agnostic)

## Error Categories

### Expected vs Unexpected

| Type | Example | How to Handle |
|------|---------|---------------|
| **Expected** | User not found, invalid input | Return error/result type, handle gracefully |
| **Unexpected** | Database down, out of memory | Throw/raise exception, log, alert |

### Recoverable vs Fatal

| Type | Example | How to Handle |
|------|---------|---------------|
| **Recoverable** | Network timeout | Retry with backoff |
| **Fatal** | Config missing, corrupt state | Fail fast, don't retry |

---

## Error Handling Patterns

### Return Error Values
```
# Explicit return of error
result, error = doSomething()
if error:
    return error

# Result type (Rust-style)
Result<User, Error> = findUser(id)
match result:
    Ok(user) -> process(user)
    Err(e) -> handleError(e)
```

**Pro:** Explicit, forces handling
**Con:** Verbose, easy to ignore

### Exceptions
```
try:
    result = doSomething()
    process(result)
catch SpecificError as e:
    handleSpecific(e)
catch Error as e:
    handleGeneric(e)
finally:
    cleanup()
```

**Pro:** Separates happy path from error path
**Con:** Can be overused, hidden control flow

### Either/Maybe Monads
```
# Maybe/Optional
Maybe<User> = findUser(id)
user.map(u -> process(u)).orElse(defaultValue)

# Either
Either<Error, User> = findUser(id)
result.fold(
    error -> handleError(error),
    user -> process(user)
)
```

**Pro:** Composable, type-safe
**Con:** Learning curve, can be verbose

---

## Error Design Principles

### Fail Fast
Detect problems as early as possible:
```
function processOrder(order) {
    # Validate first, fail immediately
    if (!order) throw new Error("Order required")
    if (!order.items) throw new Error("Order must have items")
    if (order.items.length == 0) throw new Error("Order cannot be empty")

    # Happy path continues
    ...
}
```

### Fail Loud (in development)
Make errors obvious during development:
- Detailed stack traces
- Verbose error messages
- Crash on unexpected state

### Fail Safe (in production)
Graceful degradation:
- Generic user-facing messages
- Detailed internal logs
- Fallback behaviors where appropriate

---

## Error Information

### What to Include

| Field | Purpose | Example |
|-------|---------|---------|
| `code` | Machine-readable ID | `USER_NOT_FOUND` |
| `message` | Human-readable description | "User with ID 123 not found" |
| `details` | Additional context | `{ id: 123, searched_in: "users_table" }` |
| `timestamp` | When it occurred | `2024-01-15T10:30:00Z` |
| `trace_id` | Correlation ID | `abc-123-xyz` |

### What NOT to Include (in responses)
- Stack traces
- Internal file paths
- Database queries
- System architecture details
- Credentials or tokens

---

## Custom Error Types

### Define Domain-Specific Errors
```
# Base error types
class ValidationError(Error)
class NotFoundError(Error)
class AuthorizationError(Error)
class ConflictError(Error)

# Specific errors
class UserNotFoundError(NotFoundError):
    user_id: string

class EmailAlreadyExistsError(ConflictError):
    email: string
```

### Benefits
- Clear error taxonomy
- Type-safe error handling
- Better error messages
- Easier monitoring/alerting

---

## Error Propagation

### When to Catch
- You can handle it meaningfully
- You need to transform it
- You need to add context
- You're at a boundary (API, UI)

### When to Propagate
- Higher level can handle better
- No meaningful action at this level
- Error is already well-defined

### Adding Context
```
try:
    processPayment(order)
catch PaymentError as e:
    # Add context, re-throw
    throw new OrderError(
        "Failed to process order " + order.id,
        cause=e
    )
```

---

## Retry Strategies

### When to Retry
- Transient failures (network timeout, temporary unavailability)
- Idempotent operations
- Known retriable error codes

### When NOT to Retry
- Validation errors (won't change)
- Authentication errors
- Business logic failures
- Non-idempotent operations (without idempotency key)

### Exponential Backoff
```
delay = min(base * (2 ^ attempt), max_delay)
# With jitter to avoid thundering herd
delay = delay * (0.5 + random() * 0.5)

# Example: base=100ms, max=30s
# Attempt 1: ~100ms
# Attempt 2: ~200ms
# Attempt 3: ~400ms
# ...
```

### Circuit Breaker
```
states: CLOSED -> OPEN -> HALF_OPEN -> CLOSED

CLOSED: Normal operation
OPEN: Failing, reject immediately
HALF_OPEN: Allow limited requests to test

Transition to OPEN: failure threshold exceeded
Transition to HALF_OPEN: after timeout
Transition to CLOSED: success threshold in HALF_OPEN
```

---

## Logging Errors

### What to Log
```
log.error({
    message: "Payment processing failed",
    error_code: error.code,
    order_id: order.id,
    user_id: user.id,  # (if not PII-sensitive)
    trace_id: request.trace_id,
    stack: error.stack,  # in non-production
    duration_ms: elapsed
})
```

### Log Levels for Errors
| Level | When to Use |
|-------|-------------|
| `ERROR` | Unexpected failure requiring attention |
| `WARN` | Expected failure, handled gracefully |
| `INFO` | Business error (validation failed) |

### Structured Logging
```
# BAD: unstructured
log("Error processing order 123: " + error.message)

# GOOD: structured
log.error({
    event: "order_processing_failed",
    order_id: 123,
    error: error.message
})
```

---

## Error Boundaries

### UI Error Boundaries
Catch errors in UI subtree, show fallback:
```
ErrorBoundary:
    try:
        render(children)
    catch:
        render(fallbackUI)
```

### API Error Boundaries
Global exception handler for APIs:
```
@global_exception_handler
def handle(request):
    try:
        return process(request)
    catch ValidationError as e:
        return Response(400, e.to_json())
    catch NotFoundError as e:
        return Response(404, e.to_json())
    catch Error as e:
        log.error(e)
        return Response(500, generic_error)
```

---

## Error Monitoring

### Metrics to Track
- Error rate (errors/requests)
- Error rate by type
- Error rate by endpoint
- P99 error response time

### Alerting Rules
```
# Alert if error rate > 1% for 5 minutes
alert: HighErrorRate
  when: error_rate > 0.01
  for: 5m

# Alert on specific critical errors
alert: PaymentFailure
  when: count(payment_error) > 10
  for: 1m
```

---

## User-Facing Errors

### Principles
- Be helpful, not technical
- Suggest next action
- Don't blame the user
- Provide error reference ID

### Examples
```
# BAD
"Error: ECONNREFUSED 127.0.0.1:5432"

# GOOD
"We're having trouble processing your request.
Please try again in a few minutes.
If the problem persists, contact support with reference: ABC123"
```

---

## Checklist

### Code Review
- [ ] Errors are handled, not swallowed
- [ ] Error types are appropriate
- [ ] Error messages are helpful
- [ ] Sensitive info not exposed
- [ ] Retry logic has limits
- [ ] Errors are logged

### Production Readiness
- [ ] Global error handler in place
- [ ] Error monitoring configured
- [ ] Alerts defined for critical errors
- [ ] Error responses follow standard format
- [ ] Stack traces hidden from users
