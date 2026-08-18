"""
# 70. Climbing Stairs
Difficulty: Easy
Source: https://leetcode.com/problems/climbing-stairs/

## Problem Description
You are climbing a staircase. It takes `n` steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Complexity
- Time: O(n) - Single loop up to n.
- Space: O(1) - Constant space with two variables tracking previous subproblems.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Compute number of ways to climb n stairs using DP (Fibonacci relation).
        """
        if n <= 2:
            return n

        prev1, prev2 = 1, 2
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev1, prev2 = prev2, curr

        return prev2


# =====================================================================
# Tests
# =====================================================================
def test_climb_stairs():
    sol = Solution()
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(4) == 5
    assert sol.climbStairs(5) == 8


if __name__ == "__main__":
    test_climb_stairs()
    print("All Climbing Stairs tests passed successfully! [OK]")
