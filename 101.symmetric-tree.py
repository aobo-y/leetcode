#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def check(p, q):
            if p is None and q is None:
                return True
            if p is not None and q is None:
                return False
            if p is None and q is not None:
                return False
            return p.val == q.val \
                and check(p.left, q.right) \
                and check(p.right, q.left)

        return check(root.left, root.right)

# @lc code=end

