"""
# Hash Tables: Ransom Note
Difficulty: Easy
Platform: HackerRank (Interview Preparation Kit -> Dictionaries and Hashmaps)
Source: https://www.hackerrank.com/challenges/ctci-ransom-note/problem

## Problem Description
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting.
He found a magazine and wants to know if he can cut out whole words from it and use them to untraceably replicate all the words of his ransom note!
The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.
Given the words in the magazine and the words in the ransom note, return True if he can replicate the note, or False otherwise.

## Complexity
- Time: O(m + n) - Linear time building and verifying frequency maps where m and n are words in magazine and note.
- Space: O(m) - Counter dictionary storing unique words and counts in magazine.
"""

from collections import Counter
from typing import List


def checkRansomNote(magazine: List[str], note: List[str]) -> bool:
    """
    Check if note words can be constructed entirely from magazine words.
    """
    mag_counts = Counter(magazine)
    note_counts = Counter(note)

    for word, count in note_counts.items():
        if mag_counts[word] < count:
            return False

    return True


# =====================================================================
# Tests
# =====================================================================
def test_check_ransom_note():
    mag1 = ["give", "me", "one", "grand", "today", "night"]
    note1 = ["give", "one", "grand", "today"]
    assert checkRansomNote(mag1, note1) is True

    mag2 = ["two", "times", "three", "is", "not", "four"]
    note2 = ["two", "times", "two", "is", "four"]
    assert checkRansomNote(mag2, note2) is False

    mag3 = ["ive", "got", "a", "lovely", "bunch", "of", "coconuts"]
    note3 = ["ive", "got", "some", "coconuts"]
    assert checkRansomNote(mag3, note3) is False


if __name__ == "__main__":
    test_check_ransom_note()
    print("All Ransom Note tests passed successfully! [OK]")
