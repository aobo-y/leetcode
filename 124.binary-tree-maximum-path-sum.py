#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def findMax(node):
            paths = [0]
            max_sum_cans = []
            max_val = node.val
            if node.left:
                left_max, left_path = findMax(node.left)
                max_sum_cans.append(left_max)
                if left_path > 0:
                    paths.append(left_path)
                    max_val += left_path

            if node.right:
                right_max, right_val = findMax(node.right)
                max_sum_cans.append(right_max)
                if right_val > 0:
                    paths.append(right_val)
                    max_val += right_val

            max_path = node.val + max(paths)
            max_sum_cans.append(max_val)

            return max(max_sum_cans), max_path

        max_sum, _ = findMax(root)
        return max_sum


# @lc code=end

