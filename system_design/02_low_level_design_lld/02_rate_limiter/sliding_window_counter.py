"""
# Low-Level Design: Sliding Window Counter Rate Limiter

## Theory & Algorithm
Combines the low memory footprint of Fixed Window Counter with the smoothness of Sliding Window Log.
Approximates requests in the current sliding window using:
`estimated_requests = current_window_requests + (previous_window_requests * (1 - fraction_elapsed_in_current_window))`
"""

import time
import threading
from typing import Dict


class SlidingWindowCounter:
    def __init__(self, limit: int, window_size_seconds: float = 60.0):
        self.limit = limit
        self.window_size = window_size_seconds
        self.prev_window_count = 0
        self.curr_window_count = 0
        self.current_window_start = time.time()
        self._lock = threading.Lock()

    def allow_request(self) -> bool:
        with self._lock:
            now = time.time()
            elapsed_in_current = now - self.current_window_start

            # If full window has passed, slide window forward
            if elapsed_in_current >= self.window_size:
                windows_passed = int(elapsed_in_current // self.window_size)
                if windows_passed == 1:
                    self.prev_window_count = self.curr_window_count
                else:
                    self.prev_window_count = 0

                self.curr_window_count = 0
                self.current_window_start = now - (elapsed_in_current % self.window_size)
                elapsed_in_current = now - self.current_window_start

            # Compute weighted estimate
            weight = 1.0 - (elapsed_in_current / self.window_size)
            estimated_count = self.curr_window_count + (self.prev_window_count * weight)

            if estimated_count < self.limit:
                self.curr_window_count += 1
                return True
            return False


# =====================================================================
# Tests
# =====================================================================
def test_sliding_window_counter():
    # Allow 2 requests per 0.5 second window
    limiter = SlidingWindowCounter(limit=2, window_size_seconds=0.5)

    assert limiter.allow_request() is True
    assert limiter.allow_request() is True
    assert limiter.allow_request() is False  # Limit reached

    time.sleep(0.6)  # Window shifts
    assert limiter.allow_request() is True


if __name__ == "__main__":
    test_sliding_window_counter()
    print("Sliding Window Counter LLD tests passed successfully! [OK]")
