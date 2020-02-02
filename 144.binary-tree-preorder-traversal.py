#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]

        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)

            stack.append(node.right)
            stack.append(node.left)

        return res



# @lc code=end

