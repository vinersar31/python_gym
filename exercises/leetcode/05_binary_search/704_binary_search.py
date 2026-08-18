"""
# 704. Binary Search
Difficulty: Easy
Source: https://leetcode.com/problems/binary-search/

## Problem Description
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`.
If `target` exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

## Complexity
- Time: O(log n) - Search space halved on each iteration.
- Space: O(1) - Constant auxiliary space.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Classic iterative binary search.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# =====================================================================
# Tests
# =====================================================================
def test_binary_search():
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert sol.search([5], 5) == 0
    assert sol.search([5], 0) == -1


if __name__ == "__main__":
    test_binary_search()
    print("All Binary Search tests passed successfully! [OK]")
