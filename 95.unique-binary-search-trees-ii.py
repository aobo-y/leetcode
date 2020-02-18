#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        cache = {}

        def build(left, right):
            if left > right:
                return []

            if (left, right) not in cache:
                nodes = []
                for i in range(left, right + 1):
                    for ln in build(left, i - 1) or [None]:
                        for rn in build(i + 1, right) or [None]:
                            node = TreeNode(i)
                            node.left, node.right = ln, rn
                            nodes.append(node)
                cache[(left, right)] = nodes

            return cache[(left, right)]

        return build(1, n)



# @lc code=end

