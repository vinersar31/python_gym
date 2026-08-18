# 🏛️ System Design & Distributed Systems Engineering

A complete, battle-tested System Design resource covering **Distributed Systems Fundamentals**, **Low-Level Design (LLD with runnable code)**, **High-Level Design (HLD case studies)**, and an **Interview Blueprint**.

---

## 🗂️ Module Map

```
system_design/
├── 01_fundamentals/                   # Core distributed systems principles & formulas
│   ├── 01_scalability_and_performance.md
│   ├── 02_cap_and_pacelc_theorem.md
│   ├── 03_database_scaling_and_sharding.md
│   ├── 04_caching_strategies.md
│   ├── 05_load_balancing_and_proxies.md
│   ├── 06_message_queues_and_streaming.md
│   ├── 07_back_of_envelope_estimation.md
│   └── README.md
├── 02_low_level_design_lld/           # Runnable Python OOP architectures with unit tests
│   ├── 01_lru_and_lfu_cache/          # LRU & LFU caches in O(1)
│   ├── 02_rate_limiter/               # Token Bucket & Sliding Window Counter
│   ├── 03_parking_lot/                # Multi-level garage allocation engine
│   ├── 04_in_memory_kv_store/         # Transactional KV store with nested rollback
│   ├── 05_pub_sub_broker/             # Topic broker with async subscribers
│   └── README.md
├── 03_high_level_design_hld/          # End-to-end production architecture case studies
│   ├── 01_url_shortener_tinyurl.md
│   ├── 02_distributed_rate_limiter.md
│   ├── 03_chat_system_whatsapp.md
│   ├── 04_news_feed_twitter.md
│   ├── 05_video_streaming_youtube.md
│   ├── 06_ride_sharing_uber.md
│   ├── 07_e_commerce_flash_sale.md
│   └── README.md
└── 04_interview_framework/
    └── system_design_interview_guide.md # 45-minute structured interview blueprint
```

---

## 📚 1. [Fundamentals (`01_fundamentals/`)](file:///e:/repositories/python_gym/system_design/01_fundamentals/README.md)
- **Scalability & Performance**: Horizontal vs. Vertical, Latency vs. Throughput, SLAs.
- **Theorems**: CAP & PACELC trade-off frameworks.
- **Data & Storage**: SQL vs. NoSQL, Sharding, Consistent Hashing rings.
- **Caching & Queues**: Cache-Aside, Write-Back, Kafka vs. RabbitMQ.
- **Calculations**: Latency reference chart & back-of-the-envelope estimation formulas.

---

## 📐 2. [Low-Level Design (`02_low_level_design_lld/`)](file:///e:/repositories/python_gym/system_design/02_low_level_design_lld/README.md)
Executable Python OOP architectures with complete test suites:
- **LRU & LFU Cache**: $O(1)$ Doubly Linked List + Hash Map / Frequency Buckets.
- **Rate Limiters**: Multi-tenant Token Bucket and Sliding Window Counter.
- **Parking Lot System**: Spot types, vehicle matching, ticket lifecycle.
- **In-Memory KV Store**: Full nested `begin()`, `commit()`, `rollback()` transactions.
- **Pub-Sub Broker**: Multi-topic asynchronous fan-out messaging engine.

---

## 🏛️ 3. [High-Level Design (`03_high_level_design_hld/`)](file:///e:/repositories/python_gym/system_design/03_high_level_design_hld/README.md)
Production-grade system architectures:
1. **TinyURL**: Base62 Key Generation Service (KGS) & 301/302 redirects.
2. **Distributed Rate Limiter**: Multi-region Redis cluster with atomic Lua scripts.
3. **WhatsApp / Chat**: Persistent WebSockets, Cassandra wide-column partition keys, presence tracking.
4. **Twitter News Feed**: Hybrid Fan-out on write / read to solve the celebrity problem.
5. **YouTube Streaming**: Video chunking, adaptive bitrate streaming (HLS/DASH), CDN edge caching.
6. **Uber Dispatch**: Spatial indexing (Geohashing / Uber H3 Hexagons) and driver matching.
7. **Flash Sale Engine**: Race condition mitigation, Redis atomic pre-deduction, and Saga rollback.

---

## 🎯 4. [Interview Guide (`04_interview_framework/`)](file:///e:/repositories/python_gym/system_design/04_interview_framework/system_design_interview_guide.md)
A structured 45-minute blueprint for scoping, estimating, diagramming, and troubleshooting system designs under interview conditions.
