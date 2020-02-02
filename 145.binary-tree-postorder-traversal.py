#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [(root, 0)]
        res = []

        while stack:
            node, status = stack.pop()

            if not node:
                continue

            if status == 0:
                stack.append((node, 1))
                stack.append((node.right, 0))
                stack.append((node.left, 0))
            elif status == 1:
                res.append(node.val)

        return res


# @lc code=end

