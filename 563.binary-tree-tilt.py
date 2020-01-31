#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def sum_tilt(node):
            if not node:
                return 0, 0

            left_tilt_sum, left_sum = sum_tilt(node.left)
            right_tilt_sum, right_sum = sum_tilt(node.right)

            tilt = abs(left_sum - right_sum)
            tilt_sum = left_tilt_sum + right_tilt_sum + tilt
            node_sum = left_sum  + right_sum + node.val

            return tilt_sum, node_sum

        return sum_tilt(root)[0]

# @lc code=end

