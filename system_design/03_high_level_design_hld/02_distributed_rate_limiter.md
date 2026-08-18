# ⏱️ System Design: Distributed Rate Limiter

## 1. Requirements

### Functional Requirements:
1. Limit requests per user/client IP/API key (e.g. 100 requests per minute).
2. Return HTTP `429 Too Many Requests` with `Retry-After` header when limit exceeded.
3. Support dynamic tiering (Free Tier: 10 req/min, Premium: 1,000 req/min).

### Non-Functional Requirements:
1. Low Latency overhead (< 2-5ms per request evaluation).
2. Fault Tolerance (If rate limiter fails, decide whether to open or close).
3. Consistent rate evaluation across distributed multi-region application clusters.

---

## 2. Architecture Diagram

```
[ Client ] ──> [ API Gateway / Load Balancer ]
                        │
                        ▼ (Extract API Key / User ID)
              [ Rate Limiter Middleware ]
                        │
             Atomic     ▼ (Eval Lua Script)
              [ Redis Cluster (Multi-AZ) ]
             Key: "rate_limit:user_123"
```

---

## 3. Distributed Concurrency & Race Conditions

In a distributed environment with multiple web servers processing simultaneous requests for the same user, simple `GET` followed by `SET` creates race conditions:

```
Server 1: GET count -> 4 (allowed)
Server 2: GET count -> 4 (allowed)
Server 1: SET count -> 5
Server 2: SET count -> 5  <-- Lost update! User got 2 requests counted as 1.
```

### Solution: Atomic Redis Lua Script
```lua
-- KEYS[1]: rate limit key, ARGV[1]: limit, ARGV[2]: window_seconds
local current = redis.call('incr', KEYS[1])
if current == 1 then
    redis.call('expire', KEYS[1], ARGV[2])
end
if current > tonumber(ARGV[1]) then
    return 0 -- Denied
else
    return 1 -- Allowed
end
```

---

## 4. Multi-Region Strategy & Fail-Open Behavior
- **Memory Tiering**: Use local memory cache with sliding window + periodic sync with central Redis to minimize cross-region latency.
- **Fail-Open Policy**: If Redis cluster is partitioned or unavailable, standard practice is to log error and allow requests rather than bringing down the entire platform for legitimate users.
