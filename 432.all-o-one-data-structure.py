#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#

# @lc code=start
from collections import Counter, defaultdict

class Node:
    def __init__(self, v):
        self.v = v
        self.keys = set()
        self.left = None
        self.right = None

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node_dict = {}

        self.head = Node(None)
        self.tail = Node(None)

        self.head.right = self.tail
        self.tail.left = self.head


    def __add_node(self, node, newnode):
        newnode.left = node
        newnode.right = node.right
        node.right.left = newnode
        node.right = newnode

    def __rm_node(self, node):
        node.left.right, node.right.left = node.right, node.left


    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.node_dict:
            node = self.node_dict[key]
            v = node.v
            node.keys.remove(key)
            if not node.keys:
                self.__rm_node(node)
                node = node.left
        else:
            node = self.head
            v = 0

        nv = v + 1
        if node.right.v == nv:
            newnode = node.right
        else:
            newnode = Node(nv)
            self.__add_node(node, newnode)

        newnode.keys.add(key)
        self.node_dict[key] = newnode


    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.node_dict:
            node = self.node_dict[key]
            v = node.v
            node.keys.remove(key)
            if not node.keys:
                self.__rm_node(node)

            node = node.left
        else:
            return

        nv = v - 1
        if not nv:
            del self.node_dict[key]
            return

        if node.v == nv:
            newnode = node
        else:
            newnode = Node(nv)
            self.__add_node(node, newnode)

        newnode.keys.add(key)
        self.node_dict[key] = newnode

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return next(iter(self.tail.left.keys)) if self.tail.left.keys else ''


    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(iter(self.head.right.keys)) if self.head.right.keys else ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

