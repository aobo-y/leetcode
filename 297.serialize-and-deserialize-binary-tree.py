#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize2(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        return str(root.val) + '(' + self.serialize(root.left) + ')' + '(' + self.serialize(root.right) + ')'


    def deserialize2(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        i = 0
        while data[i] != '(':
            i += 1
        node = TreeNode(int(data[:i]))

        b = 1
        j = i + 1
        while b:
            if data[j] == '(':
                b += 1
            elif data[j] == ')':
                b -= 1
            j += 1

        node.left = self.deserialize(data[i+1:j-1])
        node.right = self.deserialize(data[j+1:-1])

        return node

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        return str(root.val) + ' ' + self.serialize(root.left) + ' ' + self.serialize(root.right)


    def deserialize(self, data):
        if not data:
            return None

        tokens = data.split(' ')

        root = TreeNode(int(tokens[0]))
        node = root
        s = []

        for token in tokens[1:]:
            child = TreeNode(int(token)) if token else None
            if node:
                node.left = child
                s.append(node)
            else:
                node = s.pop()
                node.right = child

            node = child

        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

