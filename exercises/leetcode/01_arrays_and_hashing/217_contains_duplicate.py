"""
# 217. Contains Duplicate
Difficulty: Easy
Source: https://leetcode.com/problems/contains-duplicate/

## Problem Description
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Complexity
- Time: O(n) - Single pass through the array.
- Space: O(n) - Storing unique numbers in a set.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if any value appears at least twice using a hash set.
        """
        return len(nums) != len(set(nums))


# =====================================================================
# Tests
# =====================================================================
def test_contains_duplicate():
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) is True
    assert sol.containsDuplicate([1, 2, 3, 4]) is False
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


if __name__ == "__main__":
    test_contains_duplicate()
    print("All Contains Duplicate tests passed successfully! [OK]")
