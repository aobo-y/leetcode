#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        return [
            str(root.val) + '->' + p
            for p in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        ]


# @lc code=end

