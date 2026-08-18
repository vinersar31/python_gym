"""
# Time Conversion
Difficulty: Easy
Platform: HackerRank (Algorithms -> Warmup)
Source: https://www.hackerrank.com/challenges/time-conversion/problem

## Problem Description
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note:
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

## Complexity
- Time: O(1) - Fixed string length operations.
- Space: O(1) - Result string.
"""


def timeConversion(s: str) -> str:
    """
    Convert a 12-hour hh:mm:ssAM/PM string into 24-hour hh:mm:ss format.
    """
    period = s[-2:]
    hour = int(s[:2])
    minutes_seconds = s[2:-2]

    if period == "AM":
        if hour == 12:
            hour_str = "00"
        else:
            hour_str = f"{hour:02d}"
    else:  # PM
        if hour == 12:
            hour_str = "12"
        else:
            hour_str = f"{hour + 12:02d}"

    return f"{hour_str}{minutes_seconds}"


# =====================================================================
# Tests
# =====================================================================
def test_time_conversion():
    assert timeConversion("07:05:45PM") == "19:05:45"
    assert timeConversion("12:01:00PM") == "12:01:00"
    assert timeConversion("12:01:00AM") == "00:01:00"
    assert timeConversion("01:00:00AM") == "01:00:00"


if __name__ == "__main__":
    test_time_conversion()
    print("All Time Conversion tests passed successfully! [OK]")
