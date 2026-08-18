# 📈 Scalability & Performance Fundamentals

## 1. Vertical vs. Horizontal Scaling

| Aspect | Vertical Scaling (Scale Up) | Horizontal Scaling (Scale Out) |
|---|---|---|
| **Definition** | Adding more CPU, RAM, or SSDs to an existing single machine. | Adding more machines/instances into the resource pool. |
| **Hardware Limit** | Hard physical limit (e.g. 128 cores, 4TB RAM maximum). | Practically infinite capacity by adding more commodity nodes. |
| **Cost Curve** | Exponential (high-end hardware gets exponentially expensive). | Linear (standard commodity cloud VMs). |
| **Fault Tolerance** | Single Point of Failure (SPOF). Machine failure = system down. | Built-in redundancy. If one node fails, others take over. |
| **Complexity** | Simple (no distributed consensus or network partitioning). | Complex (requires load balancing, state synchronization, consistency management). |

---

## 2. Latency vs. Throughput

- **Latency**: The time required to perform an action or receive a response (measured in milliseconds `ms` or microseconds `µs`).
- **Throughput**: The number of actions or data units processed per unit time (measured in Requests Per Second `RPS` or Queries Per Second `QPS`).
- **Analogy**: A highway's speed limit determines *latency* (how fast a single car travels from A to B), while the number of lanes determines *throughput* (how many cars pass per hour).

---

## 3. High Availability (HA) & SLA (The "Nines")

Availability is calculated as: $\text{Availability} = \frac{\text{Uptime}}{\text{Uptime} + \text{Downtime}} \times 100\%$

| Availability SLA | Downtime per Year | Downtime per Month | Downtime per Day |
|---|---|---|---|
| **99% ("Two Nines")** | 3.65 days | 7.31 hours | 14.40 minutes |
| **99.9% ("Three Nines")** | 8.77 hours | 43.83 minutes | 1.44 minutes |
| **99.99% ("Four Nines")** | 52.60 minutes | 4.38 minutes | 8.64 seconds |
| **99.999% ("Five Nines")** | 5.26 minutes | 26.30 seconds | 864.00 milliseconds |
