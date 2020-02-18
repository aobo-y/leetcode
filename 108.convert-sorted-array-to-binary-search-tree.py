#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        i, j = 0, len(nums) - 1
        k = (i + j) // 2

        node = TreeNode(nums[k])
        node.left = self.sortedArrayToBST(nums[:k])
        node.right = self.sortedArrayToBST(nums[k+1:])

        return node

# @lc code=end

