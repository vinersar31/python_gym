"""
# 11. Container With Most Water
Difficulty: Medium
Source: https://leetcode.com/problems/container-with-most-water/

## Problem Description
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

## Complexity
- Time: O(n) - Two pointers moving from opposite ends toward the center.
- Space: O(1) - Constant auxiliary space.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Compute maximum water area between two lines.
        """
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


# =====================================================================
# Tests
# =====================================================================
def test_max_area():
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
    assert sol.maxArea([4, 3, 2, 1, 4]) == 16


if __name__ == "__main__":
    test_max_area()
    print("All Container With Most Water tests passed successfully! [OK]")
