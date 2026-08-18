"""
# 226. Invert Binary Tree
Difficulty: Easy
Source: https://leetcode.com/problems/invert-binary-tree/

## Problem Description
Given the `root` of a binary tree, invert the tree, and return its root.

## Complexity
- Time: O(n) - Visited every node once.
- Space: O(h) - Where h is tree height, recursive call stack O(h), worst case O(n) for skewed tree.
"""

from collections import deque
from typing import Optional, List, Any


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursively invert left and right child pointers.
        """
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# =====================================================================
# Tests
# =====================================================================
def _build_tree(values: List[Optional[Any]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def _tree_to_list(root: Optional[TreeNode]) -> List[Optional[Any]]:
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res


def test_invert_binary_tree():
    sol = Solution()
    t1 = _build_tree([4, 2, 7, 1, 3, 6, 9])
    inv1 = sol.invertTree(t1)
    assert _tree_to_list(inv1) == [4, 7, 2, 9, 6, 3, 1]

    t2 = _build_tree([2, 1, 3])
    inv2 = sol.invertTree(t2)
    assert _tree_to_list(inv2) == [2, 3, 1]

    assert sol.invertTree(None) is None


if __name__ == "__main__":
    test_invert_binary_tree()
    print("All Invert Binary Tree tests passed successfully! [OK]")
