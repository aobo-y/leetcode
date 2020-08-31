#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def toarr(node):
            if not node:
                return node
            return [node.val, toarr(node.left), toarr(node.right)]

        return str(toarr(t)) in str(toarr(s))

# @lc code=end

