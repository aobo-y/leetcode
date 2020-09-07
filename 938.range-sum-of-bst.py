#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        s = 0 if root.val > R or root.val < L else root.val
        if root.val < R:
            s += self.rangeSumBST(root.right, L, R)
        if root.val > L:
            s += self.rangeSumBST(root.left, L, R)

        return s

# @lc code=end

