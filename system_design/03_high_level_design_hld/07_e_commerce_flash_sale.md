# 🛍️ System Design: Flash Sale & High-Concurrency Inventory (Amazon / Shopee)

## 1. The Core Problem: Inventory Overselling & Race Conditions

In a flash sale (e.g. 100 PlayStation 5 units sold to 1,000,000 concurrent buyers), simultaneous database updates create severe race conditions and lock contention if not carefully architected.

```
Traditional SQL Anti-Pattern:
1. SELECT stock FROM inventory WHERE item_id = 101;  -- returns 1
2. If stock > 0:
3.    UPDATE inventory SET stock = stock - 1 WHERE item_id = 101;
-- 10,000 concurrent requests read stock = 1 before the first update completes, causing massive oversell!
```

---

## 2. Multi-Layer Mitigation Strategy

```
[ Massive Traffic Spike ]
         │
         ▼
[ Layer 1: CDN / WAF ] ──────────> Block bots, rate limit aggressive scrapers
         │
         ▼
[ Layer 2: API Gateway ] ────────> Token bucket rate limiting per user
         │
         ▼
[ Layer 3: Redis + Lua Script ] ──> In-memory Atomic Pre-Deduction (Handles 100k QPS)
         │
         ▼ (Only successful 100 orders pass)
[ Layer 4: Kafka Message Queue ] ─> Asynchronous Order Creation
         │
         ▼
[ Layer 5: Order & Payment DB ] ──> Final DB transaction with optimistic locking
```

---

## 3. Atomic Redis Pre-Deduction with Lua Script

```lua
-- KEYS[1]: item_stock_key, ARGV[1]: order_quantity
local stock = tonumber(redis.call('get', KEYS[1]))
if not stock or stock < tonumber(ARGV[1]) then
    return 0 -- Sold out / insufficient stock
end
redis.call('decrby', KEYS[1], ARGV[1])
return 1 -- Success, proceed to queue
```

---

## 4. Distributed Transaction & Saga Pattern

- If payment fails after pre-deduction:
  - Compensating transaction restores stock in Redis: `INCRBY item_stock_key quantity`.
  - Order state transitioned to `EXPIRED` / `CANCELLED`.
