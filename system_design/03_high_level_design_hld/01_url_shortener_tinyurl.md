# 🔗 System Design: URL Shortener (TinyURL / Bitly)

## 1. Requirements

### Functional Requirements:
1. Given a long URL, generate a unique short alias (e.g. `https://tiny.url/aB3x9Z`).
2. When accessing a short link, redirect user to the original long URL with HTTP 301/302.
3. Custom alias support (optional) and URL expiration (default 5 years).
4. Basic analytics (click count).

### Non-Functional Requirements:
1. High Availability (99.99%) & Low Latency (< 20ms read redirect).
2. Read-heavy system (e.g., 100:1 read-to-write ratio).
3. Short links should not be easily guessable / predictable.

---

## 2. Back-of-the-Envelope Estimation

- **Write QPS**: 100M new URLs / month $\approx 40 \text{ writes/sec}$.
- **Read QPS**: $100 \times 40 = 4,000 \text{ reads/sec}$.
- **Storage (5 Years)**: $100\text{M} \times 12 \times 5 = 6 \text{ Billion URLs}$.
  - At 500 Bytes / record $\rightarrow 6\text{B} \times 500\text{ B} = 3 \text{ TB}$.
- **Cache Memory (80/20 Rule)**: 20% of daily read requests account for 80% traffic.
  - Daily reads: $4,000 \times 86,400 \approx 345\text{M reads/day}$.
  - Cache size: $345\text{M} \times 0.20 \times 500\text{ Bytes} \approx 35 \text{ GB RAM}$.

---

## 3. Short Key Generation Architecture

Using **Base62 Encoding** (`[a-z, A-Z, 0-9]`), a 7-character string provides:
$$62^7 \approx 3.52 \text{ Trillion unique combinations}$$ (more than enough for 6B URLs).

```
                 ┌────────────────────────────────┐
                 │  Key Generation Service (KGS)  │
                 │  Pre-generates & stores tokens │
                 └───────────────┬────────────────┘
                                 │ Fetches unused keys
                                 ▼
[ Client ] ──> [ Load Balancer ] ──> [ App Web Servers ]
                                              │
                    ┌─────────────────────────┴─────────────────────────┐
                    ▼                                                   ▼
          [ Redis Cache Cluster ]                           [ Relational / NoSQL DB ]
          (Key -> Long URL mapping)                         (id, short_key, original_url, created_at)
```

---

## 4. Deep Dive: Key Generation Service (KGS) vs MD5 Hashing

- **Hashing approach**: `Base62(MD5(long_url)[:7])`. *Issue*: Collisions require appending random salt and retrying against DB.
- **KGS approach (Best)**: Standalone service generates unique 7-char random keys offline into a `keys` database table with `used` flags. When a write request arrives, the web server simply grabs an unallocated key in $O(1)$ without hashing collisions!

---

## 5. Redirect Codes: 301 vs. 302
- **301 Moved Permanently**: Browser caches redirect locally. Subsequent requests bypass TinyURL servers completely (Low server load, but loses analytics tracking).
- **302 Found (Temporary Redirect)**: Browser always routes request through TinyURL servers first (Enables accurate click analytics and rate limiting).
