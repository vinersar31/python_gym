"""
# 125. Valid Palindrome
Difficulty: Easy
Source: https://leetcode.com/problems/valid-palindrome/

## Problem Description
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Complexity
- Time: O(n) - Two pointers inward scan.
- Space: O(1) - Constant memory with in-place pointer movement.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if string is palindrome using two converging pointers.
        """
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# =====================================================================
# Tests
# =====================================================================
def test_valid_palindrome():
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome(" ") is True
    assert sol.isPalindrome("0P") is False


if __name__ == "__main__":
    test_valid_palindrome()
    print("All Valid Palindrome tests passed successfully! [OK]")
