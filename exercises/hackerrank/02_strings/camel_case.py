"""
# CamelCase
Difficulty: Easy
Platform: HackerRank (Algorithms -> Strings)
Source: https://www.hackerrank.com/challenges/camelcase/problem

## Problem Description
There is a sequence of words in CamelCase as a string of letters, `s`, having the following properties:
- It is a concatenation of one or more words consisting of English letters.
- All letters in the first word are lowercase.
- For each subsequent word, the first letter is uppercase and remaining letters are lowercase.
Given `s`, determine the number of words in `s`.

## Complexity
- Time: O(n) - Single scan counting uppercase characters.
- Space: O(1) - Counter integer.
"""


def camelcase(s: str) -> int:
    """
    Count number of words in a camelCase string.
    """
    if not s:
        return 0
    # First word starts with lowercase; each subsequent word begins with an uppercase letter
    return 1 + sum(1 for c in s if c.isupper())


# =====================================================================
# Tests
# =====================================================================
def test_camelcase():
    assert camelcase("saveChangesInTheEditor") == 5
    assert camelcase("oneTwoThree") == 3
    assert camelcase("single") == 1
    assert camelcase("") == 0


if __name__ == "__main__":
    test_camelcase()
    print("All CamelCase tests passed successfully! [OK]")
