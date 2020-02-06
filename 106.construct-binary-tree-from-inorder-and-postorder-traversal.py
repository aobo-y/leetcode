#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def build(io, po):
            if not io:
                return None

            root_val = po[-1]
            io_root_idx = io.index(root_val)

            root = TreeNode(root_val)
            root.left = build(io[:io_root_idx], po[:io_root_idx])
            root.right = build(io[io_root_idx+1:], po[io_root_idx:-1])

            return root

        return build(inorder, postorder)

# @lc code=end

