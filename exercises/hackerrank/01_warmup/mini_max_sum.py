"""
# Mini-Max Sum
Difficulty: Easy
Platform: HackerRank (Algorithms -> Warmup)
Source: https://www.hackerrank.com/challenges/mini-max-sum/problem

## Problem Description
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

## Complexity
- Time: O(n) - Calculating total sum and finding min and max in one pass.
- Space: O(1) - Constant auxiliary space.
"""

from typing import List, Tuple


def miniMaxSum(arr: List[int]) -> Tuple[int, int]:
    """
    Compute minimum and maximum sum of 4 out of 5 integers.
    """
    total = sum(arr)
    min_val = min(arr)
    max_val = max(arr)
    return total - max_val, total - min_val


# =====================================================================
# Tests
# =====================================================================
def test_mini_max_sum():
    assert miniMaxSum([1, 2, 3, 4, 5]) == (10, 14)
    assert miniMaxSum([1, 3, 5, 7, 9]) == (16, 24)
    assert miniMaxSum([5, 5, 5, 5, 5]) == (20, 20)


if __name__ == "__main__":
    test_mini_max_sum()
    print("All Mini-Max Sum tests passed successfully! [OK]")
