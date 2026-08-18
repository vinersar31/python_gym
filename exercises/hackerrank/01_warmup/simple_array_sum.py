"""
# Simple Array Sum
Difficulty: Easy
Platform: HackerRank (Algorithms -> Warmup)
Source: https://www.hackerrank.com/challenges/simple-array-sum/problem

## Problem Description
Given an array of integers, find the sum of its elements.

## Complexity
- Time: O(n) - Single linear pass.
- Space: O(1) - Constant auxiliary space.
"""

from typing import List


def simpleArraySum(ar: List[int]) -> int:
    """
    Compute the sum of elements in an array.
    """
    return sum(ar)


# =====================================================================
# Tests
# =====================================================================
def test_simple_array_sum():
    assert simpleArraySum([1, 2, 3, 4, 10, 11]) == 31
    assert simpleArraySum([]) == 0
    assert simpleArraySum([-5, 5]) == 0


if __name__ == "__main__":
    test_simple_array_sum()
    print("All Simple Array Sum tests passed successfully! [OK]")
