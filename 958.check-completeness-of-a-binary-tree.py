#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        layer = [root]

        while True:
            if None in layer:
                break

            layer = [n for node in layer for n in [node.left, node.right]]

        if any(n is None and layer[i+1] is not None for i, n in enumerate(layer[:-1])):
            return False

        if any(n.left or n.right for n in layer if n is not None):
            return False

        return True

# @lc code=end

