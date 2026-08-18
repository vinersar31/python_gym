"""
# 206. Reverse Linked List
Difficulty: Easy
Source: https://leetcode.com/problems/reverse-linked-list/

## Problem Description
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## Complexity
- Time: O(n) - Single pass through all nodes.
- Space: O(1) - Pointer manipulation in place.
"""

from typing import Optional, List, Any


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse singly linked list iteratively using three pointers (prev, curr, next).
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


# =====================================================================
# Tests
# =====================================================================
def _list_to_linked_list(elements: List[Any]) -> Optional[ListNode]:
    if not elements:
        return None
    head = ListNode(elements[0])
    curr = head
    for v in elements[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def _linked_list_to_list(head: Optional[ListNode]) -> List[Any]:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def test_reverse_list():
    sol = Solution()
    ll1 = _list_to_linked_list([1, 2, 3, 4, 5])
    rev1 = sol.reverseList(ll1)
    assert _linked_list_to_list(rev1) == [5, 4, 3, 2, 1]

    ll2 = _list_to_linked_list([1, 2])
    rev2 = sol.reverseList(ll2)
    assert _linked_list_to_list(rev2) == [2, 1]

    assert sol.reverseList(None) is None


if __name__ == "__main__":
    test_reverse_list()
    print("All Reverse Linked List tests passed successfully! [OK]")
