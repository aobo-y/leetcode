#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        layer = []
        if root:
            layer.append(root)

        while layer:
            res.append(sum(node.val for node in layer) / len(layer))
            layer = [
                n
                for node in layer
                for n in [node.left, node.right]
                if n
            ]
        return res



# @lc code=end

