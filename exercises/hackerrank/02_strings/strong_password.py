"""
# Strong Password
Difficulty: Easy
Platform: HackerRank (Algorithms -> Strings)
Source: https://www.hackerrank.com/challenges/strong-password/problem

## Problem Description
Louise joined a social networking site to stay in touch with her friends. The site requires users to input a password satisfying:
1. Length is at least 6.
2. Contains at least one digit: `0123456789`
3. Contains at least one lowercase English character: `abcdefghijklmnopqrstuvwxyz`
4. Contains at least one uppercase English character: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
5. Contains at least one special character: `!@#$%^&*()-+`

Given string `password` of length `n`, find the minimum number of characters to add to make it strong.

## Complexity
- Time: O(n) - Single pass checking presence of each character category.
- Space: O(1) - Constant sets.
"""


def minimumNumber(n: int, password: str) -> int:
    """
    Compute minimum characters needed to make password strong.
    """
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    has_digit = any(c in numbers for c in password)
    has_lower = any(c in lower_case for c in password)
    has_upper = any(c in upper_case for c in password)
    has_special = any(c in special_characters for c in password)

    missing_types = 4 - (has_digit + has_lower + has_upper + has_special)

    # Must also satisfy length >= 6
    return max(missing_types, 6 - n)


# =====================================================================
# Tests
# =====================================================================
def test_minimum_number():
    assert minimumNumber(3, "Ab1") == 3
    assert minimumNumber(11, "#HackerRank") == 1
    assert minimumNumber(7, "Au9!xyz") == 0


if __name__ == "__main__":
    test_minimum_number()
    print("All Strong Password tests passed successfully! [OK]")
