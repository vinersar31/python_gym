"""
# Luck Balance
Difficulty: Easy
Platform: HackerRank (Interview Preparation Kit -> Greedy Algorithms)
Source: https://www.hackerrank.com/challenges/luck-balance/problem

## Problem Description
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests.
Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers, `L[i]` and `T[i]`:
- `L[i]` is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by `L[i]`; if she loses it, her luck balance will increase by `L[i]`.
- `T[i]` denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.

If Lena can lose at most `k` important contests, what is the maximum luck balance she can achieve after all the preliminary contests?

## Complexity
- Time: O(n log n) - Sorting the important contests by luck value.
- Space: O(n) - Lists storing luck of important and unimportant contests.
"""

from typing import List


def luckBalance(k: int, contests: List[List[int]]) -> int:
    """
    Compute maximum luck balance Lena can achieve by losing all unimportant contests
    and losing up to k largest-luck important contests.
    """
    total_luck = 0
    important = []

    for luck, is_important in contests:
        if is_important == 0:
            total_luck += luck
        else:
            important.append(luck)

    important.sort(reverse=True)

    # Lena can lose at most k important contests (adding luck)
    # The remaining important contests she must win (subtracting luck)
    for i, luck in enumerate(important):
        if i < k:
            total_luck += luck
        else:
            total_luck -= luck

    return total_luck


# =====================================================================
# Tests
# =====================================================================
def test_luck_balance():
    contests1 = [
        [5, 1],
        [2, 1],
        [1, 1],
        [8, 1],
        [10, 0],
        [5, 0],
    ]
    # k = 3 -> Lose important contests: 8, 5, 2 (luck +15). Win: 1 (luck -1). Unimportant: 10, 5 (+15). Total = 29
    assert luckBalance(3, contests1) == 29

    contests2 = [
        [13, 1],
        [10, 1],
        [9, 1],
        [8, 1],
        [13, 1],
        [12, 1],
        [18, 1],
        [13, 1],
    ]
    assert luckBalance(5, contests2) == 42


if __name__ == "__main__":
    test_luck_balance()
    print("All Luck Balance tests passed successfully! [OK]")
