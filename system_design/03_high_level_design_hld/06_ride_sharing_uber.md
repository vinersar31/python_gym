# 🚗 System Design: Ride-Sharing Dispatch (Uber / Lyft)

## 1. Requirements

### Functional Requirements:
1. Drivers broadcast real-time GPS location periodically (every 3-5 seconds).
2. Riders request a ride, view nearby available drivers on map.
3. Match rider with the optimal nearby driver based on ETA and location.
4. Real-time trip status tracking from pickup to dropoff.

### Non-Functional Requirements:
1. Low latency (< 1s driver matching, < 500ms location broadcast ingestion).
2. High write throughput for GPS pings ($> 500,000\text{ updates/sec}$).
3. High Availability and consistency in trip state transitions.

---

## 2. Geospatial Indexing: Geohashing vs. QuadTrees

Simple SQL queries with bounding boxes (`WHERE lat BETWEEN ... AND lon BETWEEN ...`) trigger full table scans and are computationally impossible at scale.

```
                    ┌───────────────┐
                    │ World (Root)  │
                    └───┬───────┬───┘
               ┌────────┴───┐   └───┐
               ▼            ▼       ▼
             [ NW ]       [ NE ]  [ SW ]  [ SE ]
               │
          ┌────┴────┐
          ▼         ▼
       [ NW-1 ]  [ NW-2 ] (Subdivided down to ~500m precision)
```

- **Geohashing**: Encodes `(latitude, longitude)` into a Base32 string (e.g. `9q8yy`). Hierarchical property: strings with matching prefixes reside in the same geographical square!
- **Google S2 / Uber H3 (Hexagonal Indexing)**: Maps world onto hexagonal grids. Hexagons have equal distance to all 6 neighbors, preventing edge-case diagonal distortion present in squares.

---

## 3. High-Level Dispatch Architecture

```
[ Driver App ] ──(Every 3s GPS)──> [ Location Ingestion Gateway ]
                                                │
                                                ▼ (In-Memory Ephemeral Storage)
                                       [ Redis Geospatial / H3 Cluster ]
                                       Key: "geo:drivers", Value: (lat, lon, driver_id)

[ Rider App ] ──(Request Ride)──> [ Trip Management Service ]
                                                │
                                                ▼ (Query Radius $k$ km)
                                       [ Matching Engine ]
                                       - Computes ETA via Map Routing Engine
                                       - Dispatches offer to nearest driver
```
