"""
# 703. Kth Largest Element in a Stream
Difficulty: Easy
Source: https://leetcode.com/problems/kth-largest-element-in-a-stream/

## Problem Description
Design a class to find the `k-th` largest element in a stream. Note that it is the `k-th` largest element in the sorted order, not the `k-th` distinct element.
Implement `KthLargest` class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `k-th` largest element in the stream.

## Complexity
- Time: Init O(N log k), Add O(log k).
- Space: O(k) - Min-heap of fixed size k storing the k largest elements seen so far.
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# =====================================================================
# Tests
# =====================================================================
def test_kth_largest_stream():
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8


if __name__ == "__main__":
    test_kth_largest_stream()
    print("All Kth Largest in Stream tests passed successfully! [OK]")
