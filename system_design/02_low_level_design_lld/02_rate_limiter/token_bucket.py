"""
# Low-Level Design: Token Bucket Rate Limiter

## Theory & Algorithm
The Token Bucket algorithm allows a maximum burst of `capacity` tokens while continuously refilling tokens at a steady rate of `refill_rate` tokens/second.
When a request arrives:
- Compute newly generated tokens based on elapsed time: `new_tokens = elapsed * refill_rate`.
- If `tokens >= required_tokens`, allow request and deduct tokens.
- Otherwise, deny request (HTTP 429 Too Many Requests).
"""

import time
import threading
from typing import Dict


class TokenBucket:
    def __init__(self, capacity: float, refill_rate_per_sec: float):
        self.capacity = capacity
        self.refill_rate = refill_rate_per_sec
        self.tokens = capacity
        self.last_refill_timestamp = time.time()
        self._lock = threading.Lock()

    def allow_request(self, tokens_required: float = 1.0) -> bool:
        with self._lock:
            now = time.time()
            elapsed = now - self.last_refill_timestamp
            self.last_refill_timestamp = now

            # Refill tokens up to maximum capacity
            self.tokens = min(self.capacity, self.tokens + (elapsed * self.refill_rate))

            if self.tokens >= tokens_required:
                self.tokens -= tokens_required
                return True
            return False


class PerUserRateLimiter:
    """Multi-tenant Rate Limiter managing token buckets per user/API-key."""

    def __init__(self, capacity_per_user: float, refill_rate_per_sec: float):
        self.capacity = capacity_per_user
        self.refill_rate = refill_rate_per_sec
        self.buckets: Dict[str, TokenBucket] = {}
        self._lock = threading.Lock()

    def is_allowed(self, user_id: str) -> bool:
        with self._lock:
            if user_id not in self.buckets:
                self.buckets[user_id] = TokenBucket(self.capacity, self.refill_rate)
        return self.buckets[user_id].allow_request()


# =====================================================================
# Tests
# =====================================================================
def test_token_bucket():
    # Capacity: 3 requests, Refill: 10 requests / sec
    bucket = TokenBucket(capacity=3, refill_rate_per_sec=10)

    # 3 immediate requests should succeed
    assert bucket.allow_request() is True
    assert bucket.allow_request() is True
    assert bucket.allow_request() is True

    # 4th immediate request should be denied (burst exceeded)
    assert bucket.allow_request() is False

    # Sleep 0.2s -> generates ~2 tokens
    time.sleep(0.25)
    assert bucket.allow_request() is True


if __name__ == "__main__":
    test_token_bucket()
    print("Token Bucket Rate Limiter LLD tests passed successfully! [OK]")
