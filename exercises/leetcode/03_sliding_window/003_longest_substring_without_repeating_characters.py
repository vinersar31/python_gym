"""
# 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

## Complexity
- Time: O(n) - Sliding window with at most 2n steps (each character visited at most twice).
- Space: O(min(m, n)) - Set or map storing distinct characters in the current window.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Compute longest non-repeating substring length using sliding window with hash map.
        """
        char_index_map = {}  # char -> most recent index
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            char_index_map[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length


# =====================================================================
# Tests
# =====================================================================
def test_length_of_longest_substring():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring(" ") == 1


if __name__ == "__main__":
    test_length_of_longest_substring()
    print("All Longest Substring Without Repeating Characters tests passed successfully! [OK]")
