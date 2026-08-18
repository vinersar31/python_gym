"""
# 78. Subsets
Difficulty: Medium
Source: https://leetcode.com/problems/subsets/

## Problem Description
Given an integer array `nums` of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

## Complexity
- Time: O(n * 2^n) - Total 2^n subsets, each takes O(n) to copy into result.
- Space: O(n) - Max depth of the recursion tree.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all subsets using backtracking.
        """
        res = []
        subset = []

        def backtrack(start_index: int):
            res.append(list(subset))
            for i in range(start_index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return res


# =====================================================================
# Tests
# =====================================================================
def test_subsets():
    sol = Solution()
    res1 = sol.subsets([1, 2, 3])
    sorted_res1 = sorted([sorted(s) for s in res1])
    expected1 = sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
    assert sorted_res1 == expected1

    assert sol.subsets([0]) == [[], [0]]


if __name__ == "__main__":
    test_subsets()
    print("All Subsets tests passed successfully! [OK]")
