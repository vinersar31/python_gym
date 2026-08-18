"""
# 21. Merge Two Sorted Lists
Difficulty: Easy
Source: https://leetcode.com/problems/merge-two-sorted-lists/

## Problem Description
You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

## Complexity
- Time: O(n + m) - Single pass where n and m are lengths of list1 and list2.
- Space: O(1) - Merged in place using existing nodes.
"""

from typing import Optional, List, Any


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists using a sentinel/dummy head.
        """
        dummy = ListNode(-1)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy.next


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


def test_merge_two_sorted_lists():
    sol = Solution()
    l1 = _list_to_linked_list([1, 2, 4])
    l2 = _list_to_linked_list([1, 3, 4])
    merged = sol.mergeTwoLists(l1, l2)
    assert _linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4]

    assert sol.mergeTwoLists(None, None) is None

    l3 = _list_to_linked_list([0])
    merged3 = sol.mergeTwoLists(None, l3)
    assert _linked_list_to_list(merged3) == [0]


if __name__ == "__main__":
    test_merge_two_sorted_lists()
    print("All Merge Two Sorted Lists tests passed successfully! [OK]")
