"""
# Mars Exploration
Difficulty: Easy
Platform: HackerRank (Algorithms -> Strings)
Source: https://www.hackerrank.com/challenges/mars-exploration/problem

## Problem Description
A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
Letters in some of the SOS messages are altered by cosmic radiation during transmission.
Given the signal received by Earth as a string `s`, determine how many letters of the SOS message have been changed by radiation.

## Complexity
- Time: O(n) - Single pass checking against the expected "SOS" pattern.
- Space: O(1) - Counter integer.
"""


def marsExploration(s: str) -> int:
    """
    Count altered characters in repeated SOS sequence.
    """
    expected_pattern = "SOS"
    altered_count = 0

    for i, char in enumerate(s):
        if char != expected_pattern[i % 3]:
            altered_count += 1

    return altered_count


# =====================================================================
# Tests
# =====================================================================
def test_mars_exploration():
    assert marsExploration("SOSSPSSQSSOR") == 3
    assert marsExploration("SOSSOT") == 1
    assert marsExploration("SOSSOSSOS") == 0


if __name__ == "__main__":
    test_mars_exploration()
    print("All Mars Exploration tests passed successfully! [OK]")
