# Caching Strategies (Language-Agnostic)

## When to Cache

### Good Candidates
- Data that is read frequently, written rarely
- Expensive computations
- External API responses
- Database query results
- Static or semi-static content

### Poor Candidates
- Highly personalized data
- Frequently changing data
- Security-sensitive data
- Data that must always be fresh

---

## Caching Patterns

### Cache-Aside (Lazy Loading)
```
read(key):
    data = cache.get(key)
    if data == null:
        data = database.get(key)
        cache.set(key, data, ttl)
    return data

write(key, data):
    database.set(key, data)
    cache.delete(key)  # or cache.set(key, data)
```

**Pros:** Simple, cache only what's needed
**Cons:** Cache miss penalty, potential stale data

### Read-Through
```
# Cache handles loading
read(key):
    return cache.get(key, loader=database.get)
```

Cache automatically loads from source on miss.

**Pros:** Simpler application code
**Cons:** Requires cache that supports loaders

### Write-Through
```
write(key, data):
    cache.set(key, data)  # Cache handles DB write
```

Write to cache, cache writes to database synchronously.

**Pros:** Cache always consistent
**Cons:** Write latency, cache required for writes

### Write-Behind (Write-Back)
```
write(key, data):
    cache.set(key, data)
    # Async write to DB later
```

Write to cache, asynchronously persist to database.

**Pros:** Fast writes
**Cons:** Risk of data loss, complexity

### Refresh-Ahead
```
# Proactively refresh before expiration
if entry.ttl < threshold:
    async_refresh(key)
return entry.data
```

**Pros:** No cache miss latency
**Cons:** Complexity, may refresh unused data

---

## Cache Invalidation

### Time-Based (TTL)
```
cache.set(key, data, ttl=300)  # 5 minutes
```

**When to use:** When staleness is acceptable for a known period

### Event-Based
```
on_user_updated(user):
    cache.delete("user:" + user.id)
    cache.delete("user_list")
```

**When to use:** When freshness is critical

### Version-Based
```
cache_key = "user:" + user.id + ":v" + user.version
```

**When to use:** When you have version tracking

### Cache Stampede Prevention
When TTL expires, many requests hit database simultaneously.

**Solutions:**
```
# Lock-based
if cache.miss(key):
    if acquire_lock(key):
        data = database.get(key)
        cache.set(key, data)
        release_lock(key)
    else:
        wait_and_retry()

# Probabilistic early expiration
actual_ttl = ttl * (1 - log(random()) * beta)

# Background refresh
if ttl < threshold:
    async_refresh(key)
return stale_data
```

---

## Cache Layers

### Multi-Level Caching
```
L1: In-process cache (ms latency)
    |
L2: Distributed cache (low ms latency)
    |
L3: Database / Origin
```

### Example Flow
```
read(key):
    # Try L1 (local)
    data = local_cache.get(key)
    if data: return data

    # Try L2 (distributed)
    data = redis.get(key)
    if data:
        local_cache.set(key, data)
        return data

    # Load from origin
    data = database.get(key)
    redis.set(key, data)
    local_cache.set(key, data)
    return data
```

---

## HTTP Caching

### Cache-Control Headers
```
# Cacheable for 1 hour
Cache-Control: public, max-age=3600

# Private, browser only
Cache-Control: private, max-age=600

# No caching
Cache-Control: no-store

# Must revalidate
Cache-Control: must-revalidate
```

### ETags
```
# Response
ETag: "abc123"

# Subsequent request
If-None-Match: "abc123"

# Response if unchanged
304 Not Modified
```

### Last-Modified
```
# Response
Last-Modified: Wed, 15 Jan 2024 10:00:00 GMT

# Subsequent request
If-Modified-Since: Wed, 15 Jan 2024 10:00:00 GMT

# Response if unchanged
304 Not Modified
```

---

## Cache Key Design

### Principles
- Include all parameters that affect the result
- Use consistent format
- Avoid collisions
- Keep keys readable for debugging

### Examples
```
# User data
"user:{user_id}"
"user:123"

# User's orders with pagination
"user:{user_id}:orders:page:{page}:limit:{limit}"
"user:123:orders:page:1:limit:20"

# Search results
"search:{query_hash}:filters:{filter_hash}:sort:{sort}"

# API response
"api:{endpoint}:{params_hash}"
```

### Namespacing
```
# Prefix with service/module
"auth:session:abc123"
"catalog:product:456"
"inventory:stock:789"
```

---

## Cache Size Management

### Eviction Policies
| Policy | Description | Use When |
|--------|-------------|----------|
| **LRU** | Least Recently Used | General purpose |
| **LFU** | Least Frequently Used | Hot data matters |
| **FIFO** | First In First Out | Simple, time-based |
| **TTL** | Expire after time | Known staleness tolerance |
| **Random** | Random eviction | Simple, uniform access |

### Memory Management
```
# Set max memory
redis.config("maxmemory", "1gb")
redis.config("maxmemory-policy", "allkeys-lru")
```

---

## Distributed Caching

### Consistency Challenges
- Network partitions
- Node failures
- Race conditions

### Solutions
```
# Distributed locks
lock = redis.lock("resource:123")
if lock.acquire():
    try:
        do_work()
    finally:
        lock.release()

# Compare-and-set
if cache.cas(key, old_value, new_value):
    success()
else:
    retry_or_abort()
```

### Cache Clustering
- **Consistent hashing**: Minimize redistribution on node change
- **Replication**: Copies for availability
- **Sharding**: Distribute keys across nodes

---

## Caching Anti-Patterns

### Cache Everything
**Problem:** Memory waste, complexity
**Solution:** Cache selectively based on access patterns

### No Expiration
**Problem:** Stale data forever
**Solution:** Always set TTL

### Cache Sensitive Data
**Problem:** Security risk
**Solution:** Don't cache passwords, tokens, PII

### Ignoring Cache Failures
**Problem:** Silent errors, stale data
**Solution:** Handle cache errors, fallback to origin

### Caching Errors
**Problem:** Propagating failures
**Solution:** Don't cache error responses (or very short TTL)

---

## Monitoring

### Key Metrics
| Metric | Target | Alert If |
|--------|--------|----------|
| Hit rate | > 90% | < 70% |
| Latency (p99) | < 10ms | > 50ms |
| Memory usage | < 80% | > 90% |
| Eviction rate | Low | Spikes |

### Logging
```
log.info({
    event: "cache_hit",
    key: key,
    latency_ms: elapsed
})

log.warn({
    event: "cache_miss",
    key: key,
    reason: "expired"
})
```

---

## Cache Warming

### Strategies
```
# On startup
for key in important_keys:
    cache.set(key, database.get(key))

# Scheduled refresh
@every("5 minutes")
def warm_cache():
    for product in hot_products():
        cache.set("product:" + product.id, product)

# Predictive
# Based on upcoming traffic patterns
```

---

## Testing Caching

### What to Test
- [ ] Cache hit returns cached data
- [ ] Cache miss loads from origin
- [ ] TTL expiration works
- [ ] Invalidation clears cache
- [ ] Cache failure fallback works
- [ ] No sensitive data cached
- [ ] Cache keys are correct

### Testing Strategies
```
# Test with cache disabled
# Verify functionality works without cache

# Test cache behavior
mock_cache.get.returns(null)  # Force miss
assert database.get.called

mock_cache.get.returns(data)  # Force hit
assert not database.get.called
```

---

## Checklist

### Before Implementing
- [ ] Identified what to cache
- [ ] Chosen caching pattern
- [ ] Defined TTL strategy
- [ ] Defined invalidation strategy
- [ ] Designed cache keys

### Implementation
- [ ] Cache failures handled gracefully
- [ ] Stampede prevention in place
- [ ] Monitoring configured
- [ ] Memory limits set
- [ ] Eviction policy chosen

### Production
- [ ] Hit rate is acceptable
- [ ] Latency is acceptable
- [ ] Memory usage is stable
- [ ] No stale data issues
- [ ] Cache warms properly after restart
