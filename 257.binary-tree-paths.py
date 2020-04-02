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

        res = []

        layer = [(root, [])]

        while layer:
            new_layer = []
            for node, path in layer:
                if not node.left and not node.right:
                    res.append([*path, node])

                if node.left:
                    new_layer.append((node.left, [*path, node]))
                if node.right:
                    new_layer.append((node.right, [*path, node]))

            layer = new_layer

        return ['->'.join(str(node.val) for node in path) for path in res]


# @lc code=end

