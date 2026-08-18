"""
# 100. Same Tree
Difficulty: Easy
Source: https://leetcode.com/problems/same-tree/

## Problem Description
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Complexity
- Time: O(min(N, M)) - Number of nodes in smaller tree.
- Space: O(min(H_p, H_q)) - Call stack recursion depth.
"""

from typing import Optional


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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are structurally and value identical.
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# =====================================================================
# Tests
# =====================================================================
def test_same_tree():
    sol = Solution()

    # Tree 1: [1, 2, 3], Tree 2: [1, 2, 3]
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.isSameTree(p1, q1) is True

    # Tree 1: [1, 2], Tree 2: [1, None, 2]
    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    assert sol.isSameTree(p2, q2) is False

    # Tree 1: [1, 2, 1], Tree 2: [1, 1, 2]
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert sol.isSameTree(p3, q3) is False


if __name__ == "__main__":
    test_same_tree()
    print("All Same Tree tests passed successfully! [OK]")
