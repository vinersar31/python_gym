# 🏛️ High-Level Design (HLD) Case Studies

A structured collection of end-to-end distributed system architectural case studies, designed following real-world FAANG / Tier-1 interview standards.

---

## 🗺️ Case Studies Index

| # | System / Architecture | Case Study File | Core Architecture Focus |
|---|---|---|---|
| 1 | **TinyURL / Bitly** | [01_url_shortener_tinyurl.md](file:///e:/repositories/python_gym/system_design/03_high_level_design_hld/01_url_shortener_tinyurl.md) | Base62 encoding, Key Generation Service (KGS), 301 vs 302 redirects, Redis caching |
| 2 | **Distributed Rate Limiter** | [02_distributed_rate_limiter.md](file:///e:/repositories/python_gym/system_design/03_high_level_design_hld/02_distributed_rate_limiter.md) | Redis cluster, Atomic Lua scripts, Multi-region synchronization, Fail-open policy |
| 3 | **WhatsApp / Chat Messenger** | [03_chat_system_whatsapp.md](file:///e:/repositories/python_gym/system_design/03_high_level_design_hld/03_chat_system_whatsapp.md) | WebSockets, Cassandra wide-column partition keys, Presence server, Kafka sync queue |
| 4 | **Twitter / X News Feed** | [04_news_feed_twitter.md](file:///e:/repositories/python_gym/system_design/03_high_level_design_hld/04_news_feed_twitter.md) | Fan-out on write vs Fan-out on read, Celebrity problem hybrid model, Redis timeline cache |
| 5 | **YouTube / Netflix Video** | [05_video_streaming_youtube.md](file:///e:/repositories/python_gym/system_design/03_high_level_design_hld/05_video_streaming_youtube.md) | Video transcoding pipeline, Adaptive bitrate streaming (HLS/DASH), Edge CDN caching |
| 6 | **Uber / Ride Sharing** | [06_ride_sharing_uber.md](file:///e:/repositories/python_gym/system_design/03_high_level_design_hld/06_ride_sharing_uber.md) | Geospatial indexing (Geohash / Uber H3 Hexagons), Driver location broadcast, Dispatch engine |
| 7 | **Flash Sale / High Concurrency** | [07_e_commerce_flash_sale.md](file:///e:/repositories/python_gym/system_design/03_high_level_design_hld/07_e_commerce_flash_sale.md) | Race condition prevention, Atomic Redis pre-deduction, Kafka queueing, Saga compensation |
