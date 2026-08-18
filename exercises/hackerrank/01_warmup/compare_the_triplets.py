"""
# Compare the Triplets
Difficulty: Easy
Platform: HackerRank (Algorithms -> Warmup)
Source: https://www.hackerrank.com/challenges/compare-the-triplets/problem

## Problem Description
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
The rating for Alice's challenge is the triplet `a = [a[0], a[1], a[2]]`, and the rating for Bob's challenge is `b = [b[0], b[1], b[2]]`.
Compare points:
- If `a[i] > b[i]`, Alice receives 1 point.
- If `a[i] < b[i]`, Bob receives 1 point.
- If `a[i] == b[i]`, neither person receives a point.
Return an array of two integers representing Alice's score followed by Bob's score.

## Complexity
- Time: O(1) - Constant 3-element comparison.
- Space: O(1) - Fixed size 2-element output.
"""

from typing import List


def compareTriplets(a: List[int], b: List[int]) -> List[int]:
    """
    Compare score triplets between Alice and Bob.
    """
    alice_score = 0
    bob_score = 0

    for x, y in zip(a, b):
        if x > y:
            alice_score += 1
        elif x < y:
            bob_score += 1

    return [alice_score, bob_score]


# =====================================================================
# Tests
# =====================================================================
def test_compare_triplets():
    assert compareTriplets([5, 6, 7], [3, 6, 10]) == [1, 1]
    assert compareTriplets([17, 28, 30], [99, 16, 8]) == [2, 1]
    assert compareTriplets([1, 1, 1], [1, 1, 1]) == [0, 0]


if __name__ == "__main__":
    test_compare_triplets()
    print("All Compare the Triplets tests passed successfully! [OK]")
