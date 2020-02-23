#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        layer = [root]

        while layer:
            res.append([n.val for n in layer])
            layer = [
                n
                for node in layer
                for n in [node.left, node.right]
                if n
            ]

        return res

# @lc code=end

