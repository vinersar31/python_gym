# 📐 Low-Level Design (LLD) & Object-Oriented Architecture

A collection of complete, runnable Python implementations for classic Low-Level Design and Object-Oriented Design (OOD) interview problems.

---

## 🗂️ LLD Directory & Implementations

| Problem / System | Directory / File | Core Patterns & Data Structures |
|---|---|---|
| **LRU & LFU Cache** | [01_lru_and_lfu_cache/](file:///e:/repositories/python_gym/system_design/02_low_level_design_lld/01_lru_and_lfu_cache/) | Hash Map + Doubly Linked List $O(1)$, Frequency buckets with `OrderedDict` |
| **Rate Limiters** | [02_rate_limiter/](file:///e:/repositories/python_gym/system_design/02_low_level_design_lld/02_rate_limiter/) | Token Bucket (burst + refill rate), Sliding Window Counter |
| **Parking Lot System** | [03_parking_lot/parking_lot.py](file:///e:/repositories/python_gym/system_design/02_low_level_design_lld/03_parking_lot/parking_lot.py) | Spot & Vehicle hierarchy, multi-level allocation, ticketing & fee strategies |
| **Transactional KV Store** | [04_in_memory_kv_store/transactional_kv_store.py](file:///e:/repositories/python_gym/system_design/02_low_level_design_lld/04_in_memory_kv_store/transactional_kv_store.py) | In-memory key-value dictionary with nested `begin()`, `commit()`, and `rollback()` stack |
| **Pub-Sub Topic Broker** | [05_pub_sub_broker/pub_sub_system.py](file:///e:/repositories/python_gym/system_design/02_low_level_design_lld/05_pub_sub_broker/pub_sub_system.py) | Topic management, subscriber registry, asynchronous fan-out message dispatch |

---

## 🏃 Running Tests

Run any LLD problem standalone:
```bash
python system_design/02_low_level_design_lld/01_lru_and_lfu_cache/lru_cache.py
```
Or run all LLD tests via the `gym.py` CLI:
```bash
python gym.py test lld
```
