#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if not node:
                return -1
            lh, rh = height(node.left), height(node.right)
            if lh is None or rh is None:
                return None
            return max(lh, rh) + 1 if abs(lh - rh) <= 1 else None
        return height(root) is not None

# @lc code=end

