"""Linked list data structure helpers for tests and local problem execution."""

from typing import Optional, List, Any


class ListNode:
    """Standard singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def list_to_linked_list(elements: List[Any]) -> Optional[ListNode]:
    """Convert a Python list into a Singly Linked List and return the head node."""
    if not elements:
        return None
    head = ListNode(elements[0])
    curr = head
    for val in elements[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[Any]:
    """Convert a Singly Linked List starting at head into a standard Python list."""
    result = []
    curr = head
    visited = set()
    while curr is not None:
        if id(curr) in visited:
            raise ValueError("Cycle detected in linked list during conversion to list")
        visited.add(id(curr))
        result.append(curr.val)
        curr = curr.next
    return result
