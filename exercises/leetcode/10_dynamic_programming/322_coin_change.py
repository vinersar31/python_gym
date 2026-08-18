"""
# 322. Coin Change
Difficulty: Medium
Source: https://leetcode.com/problems/coin-change/

## Problem Description
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

## Complexity
- Time: O(amount * len(coins)) - Bottom-up DP table calculation.
- Space: O(amount) - DP array of size amount + 1.
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom-up dynamic programming coin change.
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != float("inf") else -1


# =====================================================================
# Tests
# =====================================================================
def test_coin_change():
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
    assert sol.coinChange([2, 5, 10, 1], 27) == 4


if __name__ == "__main__":
    test_coin_change()
    print("All Coin Change tests passed successfully! [OK]")
