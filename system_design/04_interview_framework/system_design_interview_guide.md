# 🎯 The 45-Minute System Design Interview Blueprint

A battle-tested 4-step framework used to systematically ace FAANG and Tier-1 Senior & Staff software engineering system design interviews.

---

## ⏱️ Recommended 45-Minute Time Breakdown

```
[ 00:00 - 05:00 ] ──> Step 1: Clarify Scope & Functional / Non-Functional Requirements
[ 05:00 - 10:00 ] ──> Step 2: Back-of-the-Envelope Calculations & Scale Estimation
[ 10:00 - 25:00 ] ──> Step 3: High-Level Architecture & Core Data Model
[ 25:00 - 40:00 ] ──> Step 4: Deep Dive into Critical Bottlenecks & Failure Modes
[ 40:00 - 45:00 ] ──> Step 5: Wrap-up, Trade-offs & Next Steps
```

---

## 📋 Step-by-Step Execution Guide

### Step 1: Understand the Problem & Establish Scope (0 - 5 min)
*Never start drawing boxes immediately. Ask clarifying questions to narrow the problem domain.*
- **Functional Requirements**:
  - What are the top 2-3 core features users need?
  - What features are explicitly out of scope for this 45-minute discussion?
- **Non-Functional Requirements**:
  - What is the expected availability (99.9% vs 99.99%)?
  - Latency targets (e.g. read latency < 50ms, write latency < 200ms)?
  - Consistency model: Strong Consistency (CP) or Eventual Consistency (AP)?

---

### Step 2: Back-of-the-Envelope Estimation (5 - 10 min)
*Calculate scale to justify why a single SQL database or server is insufficient.*
- **Daily Active Users (DAU)** $\rightarrow$ Estimate average & peak read/write **QPS**.
- **Storage Calculations**: $\text{Daily Writes} \times \text{Average Payload Size} \times 365 \times 5 \text{ years}$.
- **Network Bandwidth**: $\text{QPS} \times \text{Payload Size}$.
- **Memory (RAM) for Caching**: Apply the 80/20 rule (Cache 20% of daily read volume).

---

### Step 3: High-Level Design & APIs (10 - 25 min)
*Lay out the end-to-end data flow from client to persistent storage.*
1. **API Endpoints**: Define clear HTTP/gRPC signatures with request/response payloads.
2. **Database Schema**: Choose SQL vs NoSQL, primary keys, and partition keys.
3. **Core Architecture Diagram**:
   - Clients $\rightarrow$ DNS / CDN $\rightarrow$ Load Balancer (ALB) $\rightarrow$ Stateless App Servers $\rightarrow$ Cache (Redis) $\rightarrow$ DB Cluster.

---

### Step 4: Deep Dive & Bottleneck Resolution (25 - 40 min)
*This is where Senior/Staff engineers separate themselves by solving the hardest edge cases.*
- **Identify Single Points of Failure (SPOF)**: How does the system handle an AZ or DB primary failure?
- **Hotspot / Celebrity Problem**: How do you prevent a single hot key from overwhelming a single Redis/DB node?
- **Concurrency & Race Conditions**: How do you handle simultaneous updates (Distributed locks, atomic Lua scripts, optimistic locking)?
- **Data Partitioning & Replication Lag**: Consistent hashing, read-your-own-writes consistency.

---

### Step 5: Summary & Trade-Offs (40 - 45 min)
- Summarize the key trade-offs you made (e.g. why you chose eventual consistency over strong consistency).
- Mention operational monitoring: Telemetry (Prometheus), Distributed Tracing (Jaeger), alerting thresholds.
