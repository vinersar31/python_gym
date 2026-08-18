"""
# Two Strings
Difficulty: Easy
Platform: HackerRank (Interview Preparation Kit -> Dictionaries and Hashmaps)
Source: https://www.hackerrank.com/challenges/two-strings/problem

## Problem Description
Given two strings `s1` and `s2`, determine if they share a common substring. A substring may be as small as one character.
Return "YES" if they share a common substring, or "NO" otherwise.

## Complexity
- Time: O(a + b) - Converting both strings to character sets and computing set intersection.
- Space: O(1) - Max 26 lowercase English characters in set.
"""


def twoStrings(s1: str, s2: str) -> str:
    """
    Determine if s1 and s2 share at least one common character.
    Returns "YES" or "NO".
    """
    return "YES" if (set(s1) & set(s2)) else "NO"


# =====================================================================
# Tests
# =====================================================================
def test_two_strings():
    assert twoStrings("hello", "world") == "YES"
    assert twoStrings("hi", "world") == "NO"
    assert twoStrings("abc", "def") == "NO"
    assert twoStrings("aardvark", "apple") == "YES"


if __name__ == "__main__":
    test_two_strings()
    print("All Two Strings tests passed successfully! [OK]")
