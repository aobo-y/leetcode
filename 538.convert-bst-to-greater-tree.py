#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def greater_key(node, val):
            if not node:
                return val

            node.val += greater_key(node.right, val)
            return greater_key(node.left, node.val)

        greater_key(root, 0)
        return root
# @lc code=end

