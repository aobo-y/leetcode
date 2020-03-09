#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        total = 0
        layer = [(0, root)]

        while layer:
            new_layer = []
            for accum, node in layer:
                accum *= 10
                accum += node.val

                if not node.left and not node.right:
                    total += accum
                    continue

                if node.left:
                    new_layer.append((accum, node.left))
                if node.right:
                    new_layer.append((accum, node.right))

            layer = new_layer

        return total



# @lc code=end

