#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 0
        layer = [(0, root)]

        while layer:
            width = layer[-1][0] - layer[0][0] + 1
            max_width = max(width, max_width)

            layer = [
                (idx * 2 + (0 if b == 'left' else 1), node.left if b == 'left' else node.right)
                for idx, node in layer
                for b in ['left', 'right']
                if (node.left if b == 'left' else node.right)
            ]

        return max_width



# @lc code=end

