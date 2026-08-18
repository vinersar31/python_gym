"""
# Plus Minus
Difficulty: Easy
Platform: HackerRank (Algorithms -> Warmup)
Source: https://www.hackerrank.com/challenges/plus-minus/problem

## Problem Description
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with 6 places after the decimal.

## Complexity
- Time: O(n) - Single pass over the array.
- Space: O(1) - Three counter variables.
"""

from typing import List, Tuple


def plusMinus(arr: List[int]) -> Tuple[float, float, float]:
    """
    Calculate ratios of positive, negative, and zero numbers in the array.
    Returns (pos_ratio, neg_ratio, zero_ratio) rounded to 6 decimals.
    """
    n = len(arr)
    if n == 0:
        return 0.0, 0.0, 0.0

    pos_count = sum(1 for x in arr if x > 0)
    neg_count = sum(1 for x in arr if x < 0)
    zero_count = sum(1 for x in arr if x == 0)

    return (
        round(pos_count / n, 6),
        round(neg_count / n, 6),
        round(zero_count / n, 6),
    )


# =====================================================================
# Tests
# =====================================================================
def test_plus_minus():
    arr = [-4, 3, -9, 0, 4, 1]
    pos, neg, zero = plusMinus(arr)
    assert pos == 0.500000
    assert neg == 0.333333
    assert zero == 0.166667


if __name__ == "__main__":
    test_plus_minus()
    print("All Plus Minus tests passed successfully! [OK]")
