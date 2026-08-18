# ⚖️ Load Balancing & Proxies

## 1. Layer 4 (Transport) vs. Layer 7 (Application) Load Balancing

| Feature | Layer 4 Load Balancing (L4) | Layer 7 Load Balancing (L7) |
|---|---|---|
| **OSI Layer** | Transport Layer (TCP/UDP). | Application Layer (HTTP/HTTPS/gRPC). |
| **Routing Basis** | IP address and TCP/UDP port. | HTTP headers, cookies, URL paths, JSON payload. |
| **Performance** | Extremely fast, minimal CPU overhead (packet forwarding). | Higher CPU usage (requires full SSL termination and HTTP parsing). |
| **Capabilities** | Simple packet routing; cannot inspect cookies or URL paths. | Smart routing (e.g. `/api/video` -> Video cluster, `/api/auth` -> Auth cluster), SSL termination, gzip compression. |
| **Examples** | AWS Network Load Balancer (NLB), HAProxy (TCP mode), IPVS. | AWS Application Load Balancer (ALB), NGINX, Envoy, Traefik. |

---

## 2. Load Balancing Algorithms

1. **Round Robin**: Distributes requests sequentially across servers.
2. **Weighted Round Robin**: Assigns higher traffic portions to more capable machines.
3. **Least Connections**: Directs new traffic to the server with the fewest active TCP/HTTP connections.
4. **IP Hash**: Maps client IP to a specific server (`hash(client_ip) % N`), ensuring session stickiness without external storage.
5. **Least Response Time**: Evaluates both active connection count and historical TTFB (time-to-first-byte) latency.

---

## 3. Forward Proxy vs. Reverse Proxy

- **Forward Proxy**: Sits in front of the **client** (protects client identity, bypasses firewalls, caches outbound traffic).
- **Reverse Proxy**: Sits in front of the **backend web servers** (protects servers, terminates TLS/SSL, load balances traffic, caches static assets).
