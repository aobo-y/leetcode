#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:

        def count(node, lh=None, rh=None):
            if not node:
                return 0

            if lh is None:
                lh = 0
                n = node
                while n.left:
                    lh += 1
                    n = n.left

            if rh is None:
                rh = 0
                n = node
                while n.right:
                    rh += 1
                    n = n.right

            if lh == rh:
                return 2 ** (lh + 1) - 1

            return count(node.left, lh - 1, None) + count(node.right, None, rh - 1) + 1

        return count(root)

# @lc code=end

