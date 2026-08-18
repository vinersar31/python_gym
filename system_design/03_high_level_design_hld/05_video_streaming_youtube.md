# 🎬 System Design: Video Streaming Platform (YouTube / Netflix)

## 1. Requirements

### Functional Requirements:
1. Upload video content smoothly.
2. Stream videos with adaptive bitrate streaming (e.g. 1080p, 720p, 480p based on network speed).
3. Search and view video metadata (titles, views, likes, comments).

### Non-Functional Requirements:
1. High Availability (99.99%) & smooth video playback (minimal buffering / stutter).
2. Global low-latency video delivery using Content Delivery Networks (CDNs).
3. Massive storage scale (PB / EB range).

---

## 2. Video Ingestion & Transcoding Pipeline

Videos uploaded in raw format (e.g. 4K ProRes/MP4) cannot be streamed directly because different client devices (smartphones, TVs, laptops) require different resolutions and codecs (H.264, H.265, AV1, VP9).

```
[ Creator Upload ] ──> [ Upload Server ] ──> [ Raw Video S3 Storage ]
                                                        │
                                                        ▼ (Event Notification)
                                              [ Transcoding Task Queue ]
                                              (Kafka / AWS SQS)
                                                        │
                                                        ▼
                                              [ Transcoding Worker Fleet ]
                                              - Chunk video into 10s segments
                                              - Encode into 4K, 1080p, 720p, 480p
                                              - Generate HLS / DASH manifest (.m3u8)
                                                        │
                                                        ▼
                                              [ Processed Storage (S3) ]
                                                        │
                                                        ▼
                                              [ Global Edge CDNs (Cloudflare / CloudFront) ]
                                                        │
                                                        ▼
                                              [ Client Video Player (HLS / DASH) ]
```

---

## 3. Streaming Protocol: Adaptive Bitrate Streaming (HLS & MPEG-DASH)

- **HLS (HTTP Live Streaming)**: Chunks videos into small 2-10 second `.ts` media segments indexed in an `.m3u8` manifest file.
- **Client-Side Adaptive Logic**: The video player monitors current bandwidth and frame drops; it dynamically switches segments between 1080p and 720p mid-stream without interrupting playback.
- **Edge CDN Optimization**: 95%+ of video bytes are served directly from ISP Edge Caches closest to the viewer.
