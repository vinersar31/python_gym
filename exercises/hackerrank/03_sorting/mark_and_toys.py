"""
# Mark and Toys
Difficulty: Easy
Platform: HackerRank (Interview Preparation Kit -> Sorting)
Source: https://www.hackerrank.com/challenges/mark-and-toys/problem

## Problem Description
Mark and Jane are very happy after having their first child. Mark wants to buy some toys.
There are a number of different toys lying about, each with a price. Mark has only a certain amount to spend, and he wants to maximize the number of toys he can buy.
Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

## Complexity
- Time: O(n log n) - Sorting toy prices.
- Space: O(1) or O(n) depending on in-place sort.
"""

from typing import List


def maximumToys(prices: List[int], k: int) -> int:
    """
    Determine the maximum number of toys Mark can buy with budget k.
    """
    prices.sort()
    count = 0
    total_spent = 0

    for price in prices:
        if total_spent + price <= k:
            total_spent += price
            count += 1
        else:
            break

    return count


# =====================================================================
# Tests
# =====================================================================
def test_maximum_toys():
    assert maximumToys([1, 12, 5, 111, 200, 1000, 10], 50) == 4  # 1, 5, 10, 12 -> sum 28 <= 50
    assert maximumToys([1, 2, 3, 4], 7) == 3                      # 1, 2, 3 -> sum 6 <= 7
    assert maximumToys([3, 7, 2, 9, 4], 15) == 3                  # 2, 3, 4 -> sum 9 <= 15


if __name__ == "__main__":
    test_maximum_toys()
    print("All Mark and Toys tests passed successfully! [OK]")
