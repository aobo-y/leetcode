#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def modify(node, sum_=0):
            if node.right:
                sum_ = modify(node.right, sum_)

            sum_ += node.val
            node.val = sum_
            if node.left:
                sum_ = modify(node.left, sum_)

            return sum_

        modify(root)
        return root

# @lc code=end

