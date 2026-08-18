# Python Gym 🐍🏋️‍♂️

Welcome to **Python Gym**, an all-in-one software engineering and technical interview preparation command center.

This repository is organized into **4 core pillars** covering everything from CPython fundamentals to distributed system architectures, backed by an interactive CLI runner (`gym.py`).

---

## 🏛️ The 4 Repository Pillars

```
python_gym/
├── gym.py                                 # ⚡ Interactive CLI (test runner, daily challenges, stats)
├── theory/                                # 📖 1. Core Python & Computer Science Theory
│   ├── learn_the_basics/                  # 18 notebooks: syntax, data types, control flow, typing
│   ├── data_structures_and_algorithms/    # 15 notebooks: memory layout, trees, heaps, DP, sorting
│   ├── concurrency/                       # Threading, multiprocessing, asyncio, GIL mechanics
│   ├── object_oriented_programming/       # MRO, descriptors, encapsulation, dataclasses
│   ├── package_manager/                   # Pip, requirements, modern uv packaging
│   └── fast_api/                          # Asynchronous web APIs, Pydantic data schemas
├── exercises/                             # 🧠 2. Algorithmic Coding Challenges & Test Suites
│   ├── leetcode/                          # Pattern-based Blind 75 / NeetCode 150 tracks
│   ├── hackerrank/                        # Problem Solving & Interview Preparation Kit tracks
│   └── utils/                             # Shared ListNode, TreeNode & serializer helpers
├── design_patterns/                       # 🧩 3. Gang of Four (GoF) & Pythonic Design Patterns
│   ├── 01_creational/                     # Factory Method, Abstract Factory, Builder, Prototype, Singleton
│   ├── 02_structural/                     # Adapter, Composite, Decorator, Facade, Proxy
│   └── 03_behavioral/                     # Chain of Responsibility, Command, Observer, State, Strategy
└── system_design/                         # 📐 4. Distributed Systems & System Design
    ├── 01_fundamentals/                   # Scalability, CAP theorem, Sharding, Caching, MQs, Estimations
    ├── 02_low_level_design_lld/           # Runnable Python OOP (LRU/LFU cache, Rate limiter, Parking lot, KV store)
    ├── 03_high_level_design_hld/          # End-to-end case studies (TinyURL, WhatsApp, Twitter, YouTube, Uber, Flash Sale)
    └── 04_interview_framework/            # 45-minute structured interview blueprint
```

---

## ⚡ Interactive Gym CLI (`gym.py`)

Python Gym includes a built-in terminal CLI to streamline interview preparation:

```bash
# 🧪 Run all automated test suites (Exercises + Design Patterns + LLD)
python gym.py test

# 🎯 Target specific tracks
python gym.py test leetcode
python gym.py test hackerrank
python gym.py test patterns
python gym.py test lld

# 🎲 Pick a random daily interview challenge with a single command
python gym.py daily

# 📊 View full curriculum inventory and statistics
python gym.py stats

# 📚 List all curriculum modules
python gym.py list
```

---

## 🗺️ Pillar Overviews & Quick Links

### 1. 📖 [Theory & Python Mastery (`theory/`)](file:///e:/repositories/python_gym/theory/README.md)
Over 45+ interactive Jupyter notebooks covering:
- **[Learn the Basics](file:///e:/repositories/python_gym/theory/learn_the_basics/README.md)**: Variables, slicing, generator expressions, list comprehensions, typing protocols, context managers.
- **[Data Structures & Algorithms](file:///e:/repositories/python_gym/theory/data_structures_and_algorithms/README.md)**: Dynamic array resizing, custom HashMaps, Monotonic Stacks, Heaps, BSTs, and Recursion.
- **[Concurrency](file:///e:/repositories/python_gym/theory/concurrency/README.md)**: GIL bypass, CPU-bound multiprocessing, I/O-bound asyncio event loops, ThreadPoolExecutors.
- **[OOP](file:///e:/repositories/python_gym/theory/object_oriented_programming/README.md)**: Method binding protocols, C3 Linearization (MRO), Descriptors, and Abstract Base Classes.
- **[Package Manager](file:///e:/repositories/python_gym/theory/package_manager/README.md)**: Modern dependency resolution with `uv` and `pip`.
- **[FastAPI](file:///e:/repositories/python_gym/theory/fast_api/README.md)**: Asynchronous REST endpoints, Pydantic schemas, and Uvicorn.

---

### 2. 🧠 [Algorithmic Practice (`exercises/`)](file:///e:/repositories/python_gym/exercises/README.md)
Canonical coding challenges categorized by transferable problem-solving patterns:
- **[LeetCode Patterns](file:///e:/repositories/python_gym/exercises/leetcode/README.md)**: Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary Search, Linked Lists, Trees, Heaps, Backtracking, Dynamic Programming.
- **[HackerRank Tracks](file:///e:/repositories/python_gym/exercises/hackerrank/README.md)**: Warmup, Strings, Sorting, Greedy Algorithms, Dictionaries & Hash Maps.
- **[Data Structure Helpers](file:///e:/repositories/python_gym/exercises/utils/)**: Prebuilt `ListNode`, `TreeNode`, and tree deserializers for rapid testing.

---

### 3. 🧩 [Design Patterns Catalog (`design_patterns/`)](file:///e:/repositories/python_gym/design_patterns/README.md)
Executable Python implementations of classic GoF patterns with unit tests:
- **Creational**: Factory Method, Abstract Factory, Builder, Prototype, Singleton.
- **Structural**: Adapter, Composite, Decorator, Facade, Proxy.
- **Behavioral**: Chain of Responsibility, Command (Undo/Redo), Observer (Pub-Sub), State Machine, Strategy.

---

### 4. 📐 [System Design & Distributed Systems (`system_design/`)](file:///e:/repositories/python_gym/system_design/README.md)
Everything needed to master System Design interviews:
- **[01. Fundamentals](file:///e:/repositories/python_gym/system_design/01_fundamentals/README.md)**: CAP/PACELC theorems, Database sharding, Consistent Hashing, Caching strategies, Message queues, and Latency estimation cheat sheets.
- **[02. Low-Level Design (LLD)](file:///e:/repositories/python_gym/system_design/02_low_level_design_lld/README.md)**: Runnable Python OOP code for LRU/LFU Caches, Multi-Tenant Rate Limiters, Multi-Level Parking Lots, Transactional Key-Value Stores with Rollback, and Pub-Sub Brokers.
- **[03. High-Level Design (HLD)](file:///e:/repositories/python_gym/system_design/03_high_level_design_hld/README.md)**: Deep-dive production architectures for TinyURL, Distributed Rate Limiters, WhatsApp Chat, Twitter News Feed, YouTube Streaming, Uber Ride Matching, and Flash Sale Inventory Engines.
- **[04. Interview Blueprint](file:///e:/repositories/python_gym/system_design/04_interview_framework/system_design_interview_guide.md)**: A structured 45-minute guide to ace the system design interview.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+**
- **Jupyter Notebook / JupyterLab** or **VS Code / Antigravity IDE**

### Run Verification Tests
```bash
python gym.py test
```

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).