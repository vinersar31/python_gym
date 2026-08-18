"""
# 141. Linked List Cycle
Difficulty: Easy
Source: https://leetcode.com/problems/linked-list-cycle/

## Problem Description
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.
Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

## Complexity
- Time: O(n) - Floyd's Tortoise and Hare cycle detection algorithm.
- Space: O(1) - Two pointer constant auxiliary space.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect cycle using slow and fast pointer pointers.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False


# =====================================================================
# Tests
# =====================================================================
def test_has_cycle():
    sol = Solution()

    # List with cycle: 3 -> 2 -> 0 -> -4 -> (points back to 2)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    assert sol.hasCycle(n1) is True

    # List without cycle: 1 -> 2
    a1 = ListNode(1)
    a2 = ListNode(2)
    a1.next = a2
    assert sol.hasCycle(a1) is False

    # Single node without cycle
    assert sol.hasCycle(ListNode(1)) is False
    assert sol.hasCycle(None) is False


if __name__ == "__main__":
    test_has_cycle()
    print("All Linked List Cycle tests passed successfully! [OK]")
