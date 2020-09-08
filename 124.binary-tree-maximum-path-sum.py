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
        def findMax(node):  # return max sum, max single path sum
            if not node:
                return float('-inf'), float('-inf')

            l_max, l_single_sum = findMax(node.left)
            r_max, r_single_sum = findMax(node.right)

            l_single_sum, r_single_sum = max(0, l_single_sum), max(0, r_single_sum)  # allow no child path

            single_sum = node.val + max(l_single_sum, r_single_sum)
            combined_sum = node.val + l_single_sum + r_single_sum

            return max(combined_sum, l_max, r_max), single_sum

        max_sum, _ = findMax(root)
        return max_sum


# @lc code=end

