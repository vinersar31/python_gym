"""
# 33. Search in Rotated Sorted Array
Difficulty: Medium
Source: https://leetcode.com/problems/search-in-rotated-sorted-array/

## Problem Description
There is an integer array `nums` sorted in ascending order (with distinct values).
Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (1 <= k < nums.length).
Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or -1 if it is not in `nums`.
You must write an algorithm with O(log n) runtime complexity.

## Complexity
- Time: O(log n) - Modified binary search determining which half is sorted.
- Space: O(1) - Constant auxiliary space.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search on a rotated sorted array by identifying sorted half.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# =====================================================================
# Tests
# =====================================================================
def test_search_rotated_array():
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([1], 0) == -1
    assert sol.search([1], 1) == 0
    assert sol.search([3, 1], 1) == 1


if __name__ == "__main__":
    test_search_rotated_array()
    print("All Search in Rotated Sorted Array tests passed successfully! [OK]")
