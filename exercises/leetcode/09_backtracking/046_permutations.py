"""
# 46. Permutations
Difficulty: Medium
Source: https://leetcode.com/problems/permutations/

## Problem Description
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

## Complexity
- Time: O(n * n!) - Total n! permutations generated, taking O(n) to construct each.
- Space: O(n) - Recursion call stack and visited tracking set.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations via backtracking with visited tracking.
        """
        res = []
        current = []
        visited = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                res.append(list(current))
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    current.append(nums[i])
                    backtrack()
                    current.pop()
                    visited[i] = False

        backtrack()
        return res


# =====================================================================
# Tests
# =====================================================================
def test_permute():
    sol = Solution()
    res1 = sol.permute([1, 2, 3])
    sorted_res1 = sorted(res1)
    expected1 = sorted(
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
    )
    assert sorted_res1 == expected1

    assert sol.permute([0, 1]) == [[0, 1], [1, 0]]
    assert sol.permute([1]) == [[1]]


if __name__ == "__main__":
    test_permute()
    print("All Permutations tests passed successfully! [OK]")
