#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            hl, dl = dfs(node.left)
            hr, dr = dfs(node.right)

            return max(hl, hr) + 1, max(dl, dr, hl + hr)

        return dfs(root)[1]

# @lc code=end

