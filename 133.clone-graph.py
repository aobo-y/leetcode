#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_map = {}

        def clone_node(node_):
            if not node_:
                return None

            if node_ not in node_map:
                new_node = Node(node_.val)
                node_map[node_] = new_node

                new_node.neighbors = [clone_node(n) for n in node_.neighbors]

            return node_map[node_]

        return clone_node(node)
# @lc code=end

