#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ht = {}

        def copy(node):
            if not node:
                return node
            if node in ht:
                return ht[node]

            newNode = Node(node.val)
            ht[node] = newNode

            newNode.next = copy(node.next)
            newNode.random = copy(node.random)

            return newNode

        return copy(head)

# @lc code=end

