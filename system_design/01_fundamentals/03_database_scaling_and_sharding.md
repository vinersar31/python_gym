# 🗄️ Database Scaling, Replication & Sharding

## 1. Relational (SQL) vs. Non-Relational (NoSQL)

| Feature | Relational (SQL - Postgres, MySQL) | NoSQL (Document, Key-Value, Columnar, Graph) |
|---|---|---|
| **Data Model** | Structured tables, fixed schema, ACID transactions. | Flexible JSON documents, Key-Value pairs, Wide-columns. |
| **Scaling** | Primarily vertical; horizontal scaling via sharding/read-replicas is complex. | Built from the ground up for horizontal scale-out across clusters. |
| **Best For** | Financial ledgers, complex multi-table `JOIN`s, strict ACID constraints. | High write throughput, fast key lookups, rapidly evolving schemas, massive unstructured data. |

---

## 2. Replication Strategies

```
[Write Requests] ──> [ Primary (Leader) Node ]
                            │
               Replication  ▼ (Async / Semi-Sync)
        ┌───────────────────┴───────────────────┐
        ▼                                       ▼
 [ Secondary 1 (Read Replica) ]     [ Secondary 2 (Read Replica) ]
```

- **Master-Slave (Primary-Replica)**: All writes go to the Primary node. Reads are distributed across multiple read replicas.
- **Replication Lag & Solutions**:
  - *Read-your-own-writes consistency*: Route queries from the authoring user back to the primary node for 5-10 seconds after a write.

---

## 3. Database Sharding & Partitioning

Dividing a large database horizontally into smaller, independent databases called **Shards**.

### Sharding Strategies:
1. **Range-Based Sharding**: Sharding by alphabetical ranges (e.g. A-D on Shard 1) or ID ranges (1-1,000,000 on Shard 1). *Risk: Uneven distribution (Hotspots).*
2. **Hash-Based Sharding**: `shard_id = hash(sharding_key) % num_shards`. Uniform distribution. *Risk: Resharding requires moving all data when `num_shards` changes.*
3. **Consistent Hashing**: Maps both nodes and keys onto a virtual $2^{32}-1$ hash ring with virtual nodes. When a node is added/removed, only $\frac{K}{N}$ keys are relocated on average!
