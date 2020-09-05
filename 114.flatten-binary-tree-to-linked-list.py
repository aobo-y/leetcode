#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node:
                return

            l, r = node.left, node.right
            node.left, node.right = None, node.left
            l_tail, r_tail = dfs(l), dfs(r)
            if not l_tail:
                l_tail = node
            l_tail.right = r
            if not r_tail:
                r_tail = l_tail

            return r_tail

        dfs(root)

# @lc code=end

