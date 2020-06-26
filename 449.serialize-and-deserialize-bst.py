#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json
class Codec:
    def node_to_ary_2(self, node):
        if not node:
            return None

        return [node.val, self.node_to_ary(node.left), self.node_to_ary(node.right)]

    def ary_to_node_2(self, ary):
        if not ary:
            return None

        node = TreeNode(ary[0])
        node.left = self.ary_to_node(ary[1])
        node.right = self.ary_to_node(ary[2])
        return node

    def serialize_2(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        return json.dumps(self.node_to_ary(root))


    def deserialize_2(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        return self.ary_to_node(json.loads(data))


    def node_to_ary(self, node, ary):
        if not node:
            return []

        ary.append(node.val)
        self.node_to_ary(node.left, ary)
        self.node_to_ary(node.right, ary)
        return ary

    def ary_to_node(self, ary, l=0, r=None):
        if not ary:
            return None

        if r is None:
            r = len(ary)

        if l >= r:
            return None

        node = TreeNode(ary[l])
        i = l + 1
        while i < r:
            if ary[i] > ary[l]:
                break
            i += 1

        node.left = self.ary_to_node(ary, l=l + 1, r=i)
        node.right = self.ary_to_node(ary, l=i, r=r)
        return node

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        return ' '.join(str(i) for i in self.node_to_ary(root, []))


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        return self.ary_to_node([int(i) for i in data.split()])
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

