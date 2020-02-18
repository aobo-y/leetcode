#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = root
        stack = []

        while node or stack:
            if not node:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                node = node.right
            else:
                stack.append(node)
                node = node.left

# @lc code=end

