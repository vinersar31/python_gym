"""
# 1. Two Sum
Difficulty: Easy
Source: https://leetcode.com/problems/two-sum/

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

## Complexity
- Time: O(n) - Single pass through the array with hash map lookups.
- Space: O(n) - Storing visited values and their indices in a hash map.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices such that nums[i] + nums[j] == target.
        """
        seen = {}  # val -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


# =====================================================================
# Tests
# =====================================================================
def test_two_sum():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    test_two_sum()
    print("All Two Sum tests passed successfully! [OK]")
