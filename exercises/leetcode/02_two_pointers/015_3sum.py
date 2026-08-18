"""
# 15. 3Sum
Difficulty: Medium
Source: https://leetcode.com/problems/3sum/

## Problem Description
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
Notice that the solution set must not contain duplicate triplets.

## Complexity
- Time: O(n^2) - Sorting takes O(n log n), followed by nested two-pointer searches taking O(n^2).
- Space: O(1) or O(n) depending on the sorting implementation memory.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets that sum to zero.
        """
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # Skip positive numbers as sum cannot be zero
            if nums[i] > 0:
                break
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate left and right values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return res


# =====================================================================
# Tests
# =====================================================================
def test_three_sum():
    sol = Solution()
    res1 = sol.threeSum([-1, 0, 1, 2, -1, -4])
    sorted_res1 = sorted([sorted(t) for t in res1])
    expected1 = sorted([[-1, -1, 2], [-1, 0, 1]])
    assert sorted_res1 == expected1

    assert sol.threeSum([0, 1, 1]) == []
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]


if __name__ == "__main__":
    test_three_sum()
    print("All 3Sum tests passed successfully! [OK]")
