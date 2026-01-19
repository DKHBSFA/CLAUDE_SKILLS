# API Design Principles (Language-Agnostic)

## REST Conventions

### Resource Naming
```
Nouns, not verbs:     /users      (not /getUsers)
Plural form:          /users      (not /user)
Hierarchical:         /users/{id}/orders
Lowercase, hyphens:   /user-profiles (not /userProfiles)
```

### HTTP Methods Semantics

| Method | Purpose | Idempotent | Safe | Request Body |
|--------|---------|------------|------|--------------|
| GET | Read resource(s) | Yes | Yes | No |
| POST | Create resource | No | No | Yes |
| PUT | Replace resource | Yes | No | Yes |
| PATCH | Partial update | Yes | No | Yes |
| DELETE | Remove resource | Yes | No | Optional |

### Status Codes

| Range | Meaning | Common Codes |
|-------|---------|--------------|
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 4xx | Client Error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 422 Unprocessable |
| 5xx | Server Error | 500 Internal, 502 Bad Gateway, 503 Unavailable |

### Status Code Decision Tree

```
Request succeeded?
|-- No -> Is it client's fault?
|   |-- Yes -> 4xx
|   |   |-- Missing auth? -> 401
|   |   |-- Has auth but not allowed? -> 403
|   |   |-- Resource not found? -> 404
|   |   |-- Validation failed? -> 422 (or 400)
|   |   |-- Bad request format? -> 400
|   |-- No -> 5xx
|       |-- Our server error? -> 500
|       |-- Upstream error? -> 502
|       |-- Overloaded? -> 503
|-- Yes -> 2xx
    |-- Created new resource? -> 201
    |-- No content to return? -> 204
    |-- Returning data? -> 200
```

---

## Response Format Standard

### Success Response
```json
{
  "success": true,
  "data": { ... } | [ ... ],
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "hasMore": true
  }
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email format is invalid",
    "details": {
      "field": "email",
      "value": "not-an-email",
      "constraint": "email_format"
    }
  }
}
```

### Consistency Rules
- Sempre lo stesso formato per successo/errore
- `data` e sempre un oggetto o array (mai primitivo top-level)
- `error.code` e machine-readable (UPPER_SNAKE_CASE)
- `error.message` e human-readable

---

## Pagination Strategies

### Offset-based (Simple)
```
GET /users?limit=20&offset=40
```
- **Pro:** Semplice, permette jump to page
- **Con:** Problemi con dati che cambiano, lento su dataset grandi

### Cursor-based (Scalable)
```
GET /users?limit=20&cursor=abc123
```
- **Pro:** Consistente, performante
- **Con:** No jump to page

### Keyset (Highly Scalable)
```
GET /users?limit=20&after_id=500
```
- **Pro:** Molto performante con indici
- **Con:** Richiede campo ordinabile unico

### Pagination Response
```json
{
  "data": [...],
  "meta": {
    "pagination": {
      "page": 2,
      "limit": 20,
      "total": 100,
      "totalPages": 5,
      "hasNext": true,
      "hasPrev": true,
      "nextCursor": "abc123"
    }
  }
}
```

---

## Filtering, Sorting, Searching

### Filtering
```
GET /users?status=active&role=admin
GET /users?created_after=2024-01-01
GET /users?age[gte]=18&age[lte]=65
```

### Sorting
```
GET /users?sort=created_at        # ascending (default)
GET /users?sort=-created_at       # descending (prefix -)
GET /users?sort=role,-created_at  # multiple fields
```

### Searching
```
GET /users?q=john              # full-text search
GET /users?search[name]=john   # field-specific
```

### Field Selection (Sparse Fieldsets)
```
GET /users?fields=id,name,email
GET /users?fields[users]=id,name&fields[orders]=id,total
```

---

## Versioning Strategies

| Strategy | Example | Pro | Con |
|----------|---------|-----|-----|
| URL Path | `/api/v1/users` | Chiaro, cacheable | URL diversi |
| Header | `Accept-Version: 1` | URL puliti | Meno visibile |
| Query | `/api/users?v=1` | Semplice | Meno RESTful |

**Raccomandazione:** URL Path per semplicita e debugging.

### Breaking Changes
Queste richiedono nuova versione:
- Rimuovere endpoint
- Rimuovere campo obbligatorio dalla response
- Aggiungere campo obbligatorio alla request
- Cambiare tipo di un campo
- Cambiare semantica di un endpoint

Queste NON sono breaking:
- Aggiungere nuovo endpoint
- Aggiungere campo opzionale alla response
- Aggiungere campo opzionale alla request

---

## Rate Limiting

### Headers Standard
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640000000
Retry-After: 60
```

### Strategie
- **Fixed Window**: Reset ogni X minuti
- **Sliding Window**: Finestra mobile
- **Token Bucket**: Accumulo di "token" nel tempo

### Response quando rate limited (429)
```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many requests",
    "details": {
      "retryAfter": 60,
      "limit": 100,
      "window": "1 hour"
    }
  }
}
```

---

## Authentication Patterns

### Bearer Token (JWT)
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

### API Key
```
X-API-Key: your-api-key
# or
Authorization: ApiKey your-api-key
```

### Considerations
- Token in header, MAI in URL (logs!)
- Short-lived access tokens + refresh tokens
- Revocation strategy

---

## HATEOAS (Hypermedia)

Include links per navigazione:

```json
{
  "data": {
    "id": 123,
    "name": "John"
  },
  "links": {
    "self": "/users/123",
    "orders": "/users/123/orders",
    "profile": "/users/123/profile"
  }
}
```

**Quando usarlo:** API pubbliche, discoverability importante.
**Quando evitarlo:** API interne, client noti, overhead non giustificato.

---

## Idempotency

### Idempotency Keys (per POST non-idempotenti)
```
POST /orders
Idempotency-Key: unique-request-id-123
```

Server deve:
1. Salvare la chiave con la response
2. Se stessa chiave arriva di nuovo, ritornare response salvata
3. Chiavi scadono dopo X tempo

---

## Bulk Operations

### Option 1: Batch Endpoint
```
POST /users/batch
{
  "operations": [
    { "action": "create", "data": {...} },
    { "action": "update", "id": 1, "data": {...} },
    { "action": "delete", "id": 2 }
  ]
}
```

### Option 2: Separate Bulk Endpoints
```
POST /users/bulk-create
DELETE /users/bulk-delete
```

### Response
```json
{
  "success": true,
  "data": {
    "succeeded": 8,
    "failed": 2,
    "results": [
      { "index": 0, "success": true, "id": 123 },
      { "index": 3, "success": false, "error": {...} }
    ]
  }
}
```

---

## GraphQL Considerations

### Quando GraphQL
- Client ha bisogno di flessibilita nelle query
- Over-fetching/under-fetching sono problemi
- Molte relazioni tra entita
- Team frontend vuole autonomia

### Quando REST
- API semplice, risorse ben definite
- Caching importante (HTTP caching)
- Team piccolo, meno overhead
- Real-time non critico

---

## Error Response Best Practices

### DO
- Usa codici HTTP appropriati
- Includi error code machine-readable
- Fornisci messaggio human-readable
- Aggiungi dettagli per debugging (in dev)

### DON'T
- Non esporre stack traces in production
- Non rivelare dettagli di implementazione
- Non usare 200 per errori
- Non usare messaggi generici senza contesto

### Error Codes Convention
```
RESOURCE_NOT_FOUND
VALIDATION_ERROR
AUTHENTICATION_REQUIRED
PERMISSION_DENIED
RATE_LIMITED
INTERNAL_ERROR
SERVICE_UNAVAILABLE
```

---

## API Documentation

### Minimo richiesto
- Endpoint list con metodi
- Request/response examples
- Authentication method
- Error codes

### Best practice
- OpenAPI/Swagger spec
- Sandbox environment
- Code examples in multiple languages
- Changelog
