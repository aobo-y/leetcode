#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs_depth(node):
            if not node:
                return -1, None

            ld, ln = dfs_depth(node.left)
            rd, rn = dfs_depth(node.right)

            if ld > rd:
                return ld + 1, ln
            elif ld < rd:
                return rd + 1, rn
            else:
                return rd + 1, node

        _, target = dfs_depth(root)

        return target

# @lc code=end

