"""Binary tree data structure helpers for tests and local problem execution."""

from collections import deque
from typing import Optional, List, Any


class TreeNode:
    """Standard binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def build_tree(values: List[Optional[Any]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order traversal list (LeetCode format).
    e.g., [1, 2, 3, None, 4]
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
    i = 1
    n = len(values)

    while queue and i < n:
        node = queue.popleft()

        # Left child
        if i < n and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < n and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[Any]]:
    """
    Convert a binary tree to a level-order list representation (LeetCode format),
    trimming trailing None values.
    """
    if not root:
        return []

    result: List[Optional[Any]] = []
    queue: deque[Optional[TreeNode]] = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Trim trailing None entries
    while result and result[-1] is None:
        result.pop()

    return result
