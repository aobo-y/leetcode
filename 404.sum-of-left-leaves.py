#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        sum_ = 0

        layer = [(root, False)] # (node, is_left)
        while layer:
            sum_ += sum(
                n.val for n, is_left in layer
                if is_left and not n.left and not n.right
            )

            layer = [(n.left, True) for n, _ in layer if n.left] + [(n.right, False) for n, _ in layer if n.right]

        return sum_


# @lc code=end

