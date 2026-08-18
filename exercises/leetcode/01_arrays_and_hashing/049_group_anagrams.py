"""
# 49. Group Anagrams
Difficulty: Medium
Source: https://leetcode.com/problems/group-anagrams/

## Problem Description
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Complexity
- Time: O(N * K) - Where N is number of strings and K is max string length (using 26-element character count tuple).
- Space: O(N * K) - Hash map storing all strings grouped by their signature.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group strings by their 26-character count tuple key.
        """
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


# =====================================================================
# Tests
# =====================================================================
def test_group_anagrams():
    sol = Solution()
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = sol.groupAnagrams(input_strs)
    # Sort groups for deterministic testing comparison
    sorted_output = sorted([sorted(g) for g in output])
    expected = sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert sorted_output == expected

    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]


if __name__ == "__main__":
    test_group_anagrams()
    print("All Group Anagrams tests passed successfully! [OK]")
