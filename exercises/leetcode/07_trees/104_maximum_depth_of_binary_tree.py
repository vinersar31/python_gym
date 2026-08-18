"""
# 104. Maximum Depth of Binary Tree
Difficulty: Easy
Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Problem Description
Given the `root` of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Complexity
- Time: O(n) - Visited each node once.
- Space: O(h) - Where h is tree height, call stack depth.
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Compute tree height recursively with DFS.
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# =====================================================================
# Tests
# =====================================================================
def test_max_depth():
    sol = Solution()

    # Tree: [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert sol.maxDepth(root) == 3
    assert sol.maxDepth(TreeNode(1)) == 1
    assert sol.maxDepth(None) == 0


if __name__ == "__main__":
    test_max_depth()
    print("All Maximum Depth of Binary Tree tests passed successfully! [OK]")
