# 💬 System Design: Real-Time Chat System (WhatsApp / Messenger)

## 1. Requirements

### Functional Requirements:
1. 1-on-1 real-time messaging with low latency (< 100ms).
2. Group chats (up to 500 members).
3. Online / Offline user presence status.
4. Message delivery statuses (Sent ✓, Delivered ✓✓, Read ✓✓).
5. Offline message queuing & synchronization.

### Non-Functional Requirements:
1. High throughput & extreme scalability (500M DAU, billions of messages/day).
2. Zero message loss (durability).
3. End-to-end encryption (E2EE) security.

---

## 2. Real-Time Communication Protocol: WebSockets

- **HTTP Polling / Long Polling**: High HTTP header overhead, persistent reconnections.
- **WebSockets (Selected)**: Bi-directional, persistent, low-overhead TCP connection initiated via HTTP upgrade handshake.

---

## 3. High-Level Architecture

```
[ Sender Client ] ──(WebSocket)──> [ Chat Server A ]
                                          │
                        ┌─────────────────┴─────────────────┐
                        ▼                                   ▼
              [ Presence Server ]                 [ Message Sync Queue ]
              (Redis Cluster)                     (Apache Kafka)
                                                            │
                                                            ▼
                                                  [ Message Worker Service ]
                                                            │
                                         ┌──────────────────┴──────────────────┐
                                         ▼                                     ▼
                               [ Wide-Column Store ]                  [ Push Notification ]
                               (Apache Cassandra / HBase)              (Apple APNs / FCM)
                                         │                                     │
                                         ▼ (Lookup active gateway)             ▼ (If offline)
                               [ Chat Server B ] ──(WebSocket)──> [ Receiver Client ]
```

---

## 4. Message Storage: Why Cassandra / HBase?

- **Access Pattern**: Individual chat messages are written once, sequentially queried by conversation and timestamp, and rarely updated.
- **Relational DB limit**: Relational DBs bottleneck on massive write throughput ($> 500,000\text{ writes/sec}$) and expensive index maintenance.
- **Wide-Column Table Schema**:
  - `Partition Key`: `conversation_id` (Ensures all messages in a chat reside on the same physical node).
  - `Clustering Key`: `message_id` / `created_at` (Sorted in chronological descending order for instant pagination).
