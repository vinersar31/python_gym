"""
# Birthday Cake Candles
Difficulty: Easy
Platform: HackerRank (Algorithms -> Warmup)
Source: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

## Problem Description
You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age.
They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

## Complexity
- Time: O(n) - Single pass finding maximum height and counting its occurrences.
- Space: O(1) - Constant auxiliary space.
"""

from typing import List


def birthdayCakeCandles(candles: List[int]) -> int:
    """
    Count the number of candles that have the maximum height.
    """
    if not candles:
        return 0
    max_height = max(candles)
    return candles.count(max_height)


# =====================================================================
# Tests
# =====================================================================
def test_birthday_cake_candles():
    assert birthdayCakeCandles([4, 4, 1, 3]) == 2
    assert birthdayCakeCandles([3, 2, 1, 3]) == 2
    assert birthdayCakeCandles([1]) == 1
    assert birthdayCakeCandles([]) == 0


if __name__ == "__main__":
    test_birthday_cake_candles()
    print("All Birthday Cake Candles tests passed successfully! [OK]")
