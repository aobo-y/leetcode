#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []

        layer = [root]

        while layer:
            res.append([n.val for n in layer])
            new_layer = []

            for node in layer:
                if node.left:
                    new_layer.append(node.left)
                if node.right:
                    new_layer.append(node.right)

            layer = new_layer

        return res[::-1]

# @lc code=end

