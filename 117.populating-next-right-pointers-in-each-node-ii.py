#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        layer = []
        if root:
            layer.append(root)

        while layer:
            new_layer = []
            prev = None
            for node in layer:
                if prev:
                    prev.next = node

                prev = node
                for n in (node.left, node.right):
                    if n:
                        new_layer.append(n)

            layer = new_layer

        return root


# @lc code=end

