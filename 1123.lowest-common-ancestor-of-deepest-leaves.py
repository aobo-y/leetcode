#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node, l=0):
            if not node:
                return None, l - 1

            nl, hl = dfs(node.left, l + 1)
            nr, hr = dfs(node.right, l + 1)

            if hl > hr:
                return nl, hl
            elif hl < hr:
                return nr, hr
            else:
                return node, hl

        return dfs(root)[0]


# @lc code=end

