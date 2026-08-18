# ⚖️ CAP Theorem & PACELC Theorem

## 1. The CAP Theorem

In any asynchronous distributed data store across a network, you can only guarantee **at most two** out of the following three guarantees:

```
                  Consistency (C)
                    /         \
                   /           \
                  /    Network  \
                 /    Partition  \
    Availability (A) ------------ Partition Tolerance (P)
```

1. **Consistency (C)**: Every read receives the most recent write or an error (Linearizability).
2. **Availability (A)**: Every non-failing node returns a non-error response for every request (without guaranteeing it contains the most recent write).
3. **Partition Tolerance (P)**: The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes.

### The Real-World Choice: CP vs. AP
Because network partitions ($P$) are inevitable in physical distributed networks:
- **CP Systems** (Choose Consistency over Availability during partition): Return an error or block until the partition heals (e.g. HBase, CockroachDB, etcd, ZooKeeper, MongoDB with majority write concerns).
- **AP Systems** (Choose Availability over Consistency during partition): Return the most recent local state even if stale, and reconcile later using Eventual Consistency (e.g. Cassandra, DynamoDB, CouchDB).

---

## 2. The PACELC Theorem

The PACELC theorem extends CAP by explaining system trade-offs **even when there is NO network partition**:

> **If Partition ($P$):** Trade-off between **Availability ($A$)** and **Consistency ($C$)**.
> **Else ($E$):** Trade-off between **Latency ($L$)** and **Consistency ($C$)**.

| System | Classification | Behavior during Partition | Behavior during Normal State |
|---|---|---|---|
| **Cassandra / DynamoDB** | **PA/EL** | High Availability | Low Latency (Eventual Consistency) |
| **MongoDB / HBase** | **PC/EC** | Strong Consistency | High Consistency (Waits for replication) |
| **MySQL (Master-Slave)** | **PC/EC** | Consistent Primary | Consistent reads with replication lag |
