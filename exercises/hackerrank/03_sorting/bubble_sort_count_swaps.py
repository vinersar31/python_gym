"""
# Sorting: Bubble Sort (Count Swaps)
Difficulty: Easy
Platform: HackerRank (Interview Preparation Kit -> Sorting)
Source: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

## Problem Description
Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm.
Once sorted, determine:
1. Total number of swaps required.
2. First element in the sorted array.
3. Last element in the sorted array.

## Complexity
- Time: O(n^2) - Bubble Sort comparisons and adjacent swaps.
- Space: O(1) - In-place sorting.
"""

from typing import List, Tuple


def countSwaps(a: List[int]) -> Tuple[int, int, int]:
    """
    Run Bubble Sort, returning (num_swaps, first_element, last_element).
    """
    n = len(a)
    num_swaps = 0

    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1

    first_element = a[0] if n > 0 else 0
    last_element = a[-1] if n > 0 else 0
    return num_swaps, first_element, last_element


# =====================================================================
# Tests
# =====================================================================
def test_count_swaps():
    assert countSwaps([6, 4, 1]) == (3, 1, 6)
    assert countSwaps([1, 2, 3]) == (0, 1, 3)
    assert countSwaps([3, 2, 1]) == (3, 1, 3)


if __name__ == "__main__":
    test_count_swaps()
    print("All Bubble Sort Count Swaps tests passed successfully! [OK]")
