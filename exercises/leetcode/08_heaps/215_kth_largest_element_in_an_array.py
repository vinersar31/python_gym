"""
# 215. Kth Largest Element in an Array
Difficulty: Medium
Source: https://leetcode.com/problems/kth-largest-element-in-an-array/

## Problem Description
Given an integer array `nums` and an integer `k`, return the `k-th` largest element in the array.
Note that it is the `k-th` largest element in the sorted order, not the `k-th` distinct element.
Can you solve it without sorting?

## Complexity
- Time: O(n log k) using a Min-Heap of size k.
- Space: O(k) for the heap.
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find k-th largest element using min-heap of size k.
        """
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


# =====================================================================
# Tests
# =====================================================================
def test_find_kth_largest():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert sol.findKthLargest([1], 1) == 1


if __name__ == "__main__":
    test_find_kth_largest()
    print("All Kth Largest in Array tests passed successfully! [OK]")
