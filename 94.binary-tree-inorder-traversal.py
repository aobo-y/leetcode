#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        node = root
        res = []

        while node or stack:
            if not node:
                node = stack.pop()
                res.append(node.val)
                node = node.right

            else:
                stack.append(node)
                node = node.left

        return res



# @lc code=end

