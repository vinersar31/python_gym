# 🐦 System Design: News Feed (Twitter / X / Instagram)

## 1. Requirements

### Functional Requirements:
1. Post a new tweet / post (text, image, video).
2. Follow / Unfollow other users.
3. View home news feed (chronologically or ranked by ML relevance).

### Non-Functional Requirements:
1. Rapid feed generation (< 200ms).
2. Extremely read-heavy (e.g. 500M reads/day vs 50M writes/day).
3. Eventual consistency across followers' feeds.

---

## 2. Feed Generation Models: Push vs. Pull vs. Hybrid

### Model A: Pull (Fan-out on Read)
- When a user opens their feed, query the DB for all users they follow, retrieve their latest tweets, and merge/sort them.
- *Pros*: No write-time work.
- *Cons*: Extremely slow read latency for users following thousands of accounts ($O(N \text{ followers} \times M \text{ posts})$ query).

### Model B: Push (Fan-out on Write)
- When a user posts a tweet, proactively append the tweet ID to the Redis Timeline Cache of **every single follower**.
- *Pros*: Instant $O(1)$ read time when fetching feed.
- *Cons*: **Celebrity / Hotspot Problem**: A user with 100M followers (e.g. Elon Musk, Cristiano Ronaldo) triggers 100M write operations for a single tweet!

### Model C: Hybrid Approach (Industry Standard)
- **Normal Users (< 25,000 followers)**: Use **Fan-out on Write** (Push). Pre-generate timeline in Redis.
- **Celebrities (> 25,000 followers)**: Use **Fan-out on Read** (Pull). Do not fan out their tweets to 50M timelines. Instead, when a follower opens their feed, fetch the celebrity's recent tweets and merge them dynamically into the cached timeline.

---

## 3. Architecture Overview

```
[ User Posts Tweet ] ──> [ Tweet Service ] ──> [ Kafka Topic ]
                                                      │
                                    ┌─────────────────┴─────────────────┐
                                    ▼                                   ▼
                         [ Fan-Out Worker ]                   [ DB Storage ]
                         (Checks follower count)              (PostgreSQL / Cassandra)
                                    │
                                    ▼
                         [ Redis Timeline Cache ]
                         Key: "user_timeline:<follower_id>" -> List of Tweet IDs
```
