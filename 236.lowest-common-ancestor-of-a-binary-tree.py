#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs_path(node, v, path):
            if not node:
                return False

            path.append(node)
            if node == v or dfs_path(node.left, v, path) or dfs_path(node.right, v, path):
                return True

            path.pop()

            return False

        path_p, path_q = [], []
        dfs_path(root, p, path_p)
        dfs_path(root, q, path_q)

        return [v1 for v1, v2 in zip(path_p, path_q) if v1 == v2][-1]

# @lc code=end

