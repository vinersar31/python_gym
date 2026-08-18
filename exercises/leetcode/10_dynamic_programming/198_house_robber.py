"""
# 198. House Robber
Difficulty: Medium
Source: https://leetcode.com/problems/house-robber/

## Problem Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Complexity
- Time: O(n) - Single pass DP transition.
- Space: O(1) - Maintaining only the two prior state variables.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Compute maximum loot without robbing adjacent houses.
        DP formula: rob = max(rob1 + n, rob2)
        """
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


# =====================================================================
# Tests
# =====================================================================
def test_rob():
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
    assert sol.rob([2, 1, 1, 2]) == 4
    assert sol.rob([5]) == 5
    assert sol.rob([]) == 0


if __name__ == "__main__":
    test_rob()
    print("All House Robber tests passed successfully! [OK]")
