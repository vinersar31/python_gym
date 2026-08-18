"""
# 155. Min Stack
Difficulty: Medium
Source: https://leetcode.com/problems/min-stack/

## Problem Description
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element val onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

## Complexity
- Time: O(1) for all operations (`push`, `pop`, `top`, `getMin`).
- Space: O(n) - Auxiliary stack tracking minimum at each state.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("top from empty stack")

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("getMin from empty stack")


# =====================================================================
# Tests
# =====================================================================
def test_min_stack():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2


if __name__ == "__main__":
    test_min_stack()
    print("All Min Stack tests passed successfully! [OK]")
