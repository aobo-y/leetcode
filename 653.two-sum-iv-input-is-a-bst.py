#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        l = [root]
        vals = set()
        while l:
            for n in l:
                if k - n.val in vals:
                    return True
                vals.add(n.val)
            l = [nn for n in l for nn in [n.left, n.right] if nn]

        return False


# @lc code=end

