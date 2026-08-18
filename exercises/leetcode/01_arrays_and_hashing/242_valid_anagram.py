"""
# 242. Valid Anagram
Difficulty: Easy
Source: https://leetcode.com/problems/valid-anagram/

## Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Complexity
- Time: O(n) - Single pass character counting where n is the length of strings.
- Space: O(1) or O(k) - At most 26 lowercase English letters stored in frequency map.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if s and t have identical character counts.
        """
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


# =====================================================================
# Tests
# =====================================================================
def test_is_anagram():
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    assert sol.isAnagram("a", "ab") is False


if __name__ == "__main__":
    test_is_anagram()
    print("All Valid Anagram tests passed successfully! [OK]")
