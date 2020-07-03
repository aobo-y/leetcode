#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def right_nodes(node, ary, lv=0):
            if not node:
                return

            if lv > len(ary) - 1:
                ary.append(node.val)

            right_nodes(node.right, ary, lv + 1)
            right_nodes(node.left, ary, lv + 1)

        res = []
        right_nodes(root, res)

        return res

# @lc code=end

