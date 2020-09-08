#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, mx=float('-inf'), mn=float('inf')):
            if not node:
                return abs(mx - mn)

            mx, mn = max(mx, node.val), min(mn, node.val)
            return max(dfs(node.left, mx, mn), dfs(node.right, mx, mn))

        return dfs(root)

# @lc code=end

