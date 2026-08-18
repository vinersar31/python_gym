"""
# 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Problem Description
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Complexity
- Time: O(n) - Single pass through the prices array.
- Space: O(1) - Constant auxiliary space.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate maximum profit with dynamic min price tracking.
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# =====================================================================
# Tests
# =====================================================================
def test_max_profit():
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([2, 4, 1]) == 2


if __name__ == "__main__":
    test_max_profit()
    print("All Best Time to Buy and Sell Stock tests passed successfully! [OK]")
