"""
# 20. Valid Parentheses
Difficulty: Easy
Source: https://leetcode.com/problems/valid-parentheses/

## Problem Description
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Complexity
- Time: O(n) - Single pass through string.
- Space: O(n) - Stack for bracket matching.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Validate bracket matching using a LIFO stack.
        """
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


# =====================================================================
# Tests
# =====================================================================
def test_valid_parentheses():
    sol = Solution()
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("{[]}") is True
    assert sol.isValid("]") is False


if __name__ == "__main__":
    test_valid_parentheses()
    print("All Valid Parentheses tests passed successfully! [OK]")
