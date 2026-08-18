"""
# Minimum Absolute Difference in an Array
Difficulty: Easy
Platform: HackerRank (Interview Preparation Kit -> Greedy Algorithms)
Source: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

## Problem Description
Given an array of integers, find the minimum absolute difference between any two elements in the array.

## Complexity
- Time: O(n log n) - Sorting elements to ensure minimum absolute difference is between adjacent elements.
- Space: O(1) or O(n) depending on sort.
"""

from typing import List


def minimumAbsoluteDifference(arr: List[int]) -> int:
    """
    Find minimum absolute difference between any pair in the array.
    """
    arr.sort()
    min_diff = float("inf")

    for i in range(len(arr) - 1):
        diff = abs(arr[i + 1] - arr[i])
        if diff < min_diff:
            min_diff = diff
            if min_diff == 0:
                return 0

    return int(min_diff)


# =====================================================================
# Tests
# =====================================================================
def test_minimum_absolute_difference():
    assert minimumAbsoluteDifference([3, -7, 0]) == 3
    assert minimumAbsoluteDifference([-59, -36, -13, 1, -53, -20, 67, -79, -96, -54, -75]) == 1
    assert minimumAbsoluteDifference([1, -3, 71, 68, 17]) == 3


if __name__ == "__main__":
    test_minimum_absolute_difference()
    print("All Minimum Absolute Difference tests passed successfully! [OK]")
