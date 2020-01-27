#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        reverse = False

        layer = [root] if root else []
        res = []

        while layer:
            new_layer = []
            for node in layer:
                if node.left:
                    new_layer.append(node.left)
                if node.right:
                    new_layer.append(node.right)

            res.append([n.val for n in layer])
            if reverse:
                res[-1] = res[-1][::-1]
            reverse = not reverse
            layer = new_layer

        return res

# @lc code=end

