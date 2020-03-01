#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        nodes = [root]
        while nodes:
            for node in nodes:
                if node:
                    node.left, node.right = node.right, node.left

            nodes = [
                n
                for node in nodes if node
                for n in [node.left, node.right] if n
            ]

        return root

# @lc code=end

