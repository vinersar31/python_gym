# 📬 Message Queues & Event Streaming

## 1. Why Use Message Queues?

1. **Decoupling**: Senders and receivers operate independently without knowing each other's network addresses or availability.
2. **Buffering / Backpressure / Peak Shaving**: Absorbs spikes in user traffic (e.g. Flash sales, ticket drops) and processes them at a controlled steady rate.
3. **Asynchronous Execution**: Offload long-running tasks (video transcoding, PDF generation, email dispatch) from user-facing HTTP request-response cycles.
4. **Reliability & Resilience**: Messages persist in durable storage until consumed and acknowledged.

---

## 2. Message Queue (RabbitMQ / SQS) vs. Event Streaming (Kafka / Pulsar)

```
[ Traditional Message Queue (RabbitMQ) ]
  Producer ──> [ Point-to-Point Queue ] ──> Consumer A (Message removed once ACKed)

[ Distributed Event Stream (Apache Kafka) ]
  Producer ──> [ Append-Only Partitioned Log ] ──┬──> Consumer Group 1 (Offset 42)
                                                 └──> Consumer Group 2 (Offset 10)
```

| Feature | Message Queue (RabbitMQ / AWS SQS) | Event Stream (Apache Kafka) |
|---|---|---|
| **Data Model** | Ephemeral messages (deleted once processed and acknowledged). | Immutable, ordered append-only log retained on disk (re-playable). |
| **Consumer Tracking** | Broker tracks which consumer received which message. | Consumer maintains its own partition offset cursor. |
| **Throughput** | Moderate (10k - 50k msgs/sec). | Massive (millions of msgs/sec with sequential disk I/O). |
| **Best For** | Complex task routing, individual message ACKs, worker task queues. | Real-time analytics, event sourcing, activity feeds, log aggregation. |

---

## 3. Delivery Guarantees

- **At-Most-Once**: Messages may be lost, but never duplicated (Fire and forget).
- **At-Least-Once**: Messages are guaranteed to arrive, but may occasionally be delivered twice if ACKs fail. *(Requires idempotent consumer handling)*.
- **Exactly-Once**: Each message is effectively processed once and only once (Achieved via transactional producers + consumer idempotency/two-phase commit).
