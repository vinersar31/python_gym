# ⚡ Caching Strategies & Eviction Policies

## 1. Caching Topologies & Patterns

```
              ┌─────────┐
              │ Client  │
              └────┬────┘
                   │
           ┌───────▼───────┐
           │  Application  │
           └───┬───────┬───┘
               │       │
    (1) Check  │       │ (3) Fallback
        Cache  │       │     DB Read
               ▼       ▼
          ┌───────┐ ┌──────┐
          │ Cache │ │  DB  │
          └───────┘ └──────┘
```

### Top Caching Patterns:
1. **Cache-Aside (Lazy Loading)**:
   - App checks cache first.
   - If cache hit: Return data.
   - If cache miss: Query DB, write to cache, return data.
   - *Pros*: Only requested data is cached.
   - *Cons*: Cache miss penalty; possible stale data if DB updated directly.

2. **Read-Through**:
   - App treats cache as the main data store. Cache library fetches missing keys from DB automatically.

3. **Write-Through**:
   - App writes to cache, and cache synchronously writes to DB before returning success.
   - *Pros*: Cache and DB are always consistent.
   - *Cons*: Write latency penalty.

4. **Write-Behind (Write-Back)**:
   - App writes only to cache immediately. Cache asynchronously batches writes to DB in the background.
   - *Pros*: Extremely low write latency.
   - *Cons*: Risk of data loss if cache crashes before flushing to DB.

---

## 2. Common Cache Pitfalls & Solutions

- **Cache Stampede / Dogpiling (Thundering Herd)**: Thousands of concurrent requests hit the DB at once when a hot cache key expires.
  - *Fix*: Mutex lock (single flight) or probabilistic early refresh (XFetch algorithm).
- **Cache Penetration**: Queries for non-existent keys bypass cache and slam DB.
  - *Fix*: Cache `None`/null values with a short TTL, or use a **Bloom Filter**.
- **Cache Avalanche**: Many keys expire at the exact same second.
  - *Fix*: Add random jitter to TTLs: `TTL = base_ttl + random.randint(-60, 60)`.
