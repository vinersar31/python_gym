"""
# Staircase
Difficulty: Easy
Platform: HackerRank (Algorithms -> Warmup)
Source: https://www.hackerrank.com/challenges/staircase/problem

## Problem Description
This is a staircase of size n = 4:
   #
  ##
 ###
####
Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size n.

## Complexity
- Time: O(n) - Iterating n levels.
- Space: O(n) - String construction per line.
"""

from typing import List


def build_staircase(n: int) -> List[str]:
    """
    Build lines of a right-aligned staircase of size n.
    """
    return [(" " * (n - i)) + ("#" * i) for i in range(1, n + 1)]


# =====================================================================
# Tests
# =====================================================================
def test_staircase():
    expected_4 = [
        "   #",
        "  ##",
        " ###",
        "####",
    ]
    assert build_staircase(4) == expected_4
    assert build_staircase(1) == ["#"]


if __name__ == "__main__":
    for line in build_staircase(6):
        print(line)
    test_staircase()
    print("All Staircase tests passed successfully! [OK]")
