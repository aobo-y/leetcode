#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pop(self):
        if not self.head:
            return None

        node = self.head
        self.remove(node)

        return node

    def remove(self, node):
        if self.head == node:
            self.head = node.right
        if self.tail == node:
            self.tail = node.left

        if node.left:
            node.left.right = node.right
        if node.right:
            node.right.left = node.left

        node.left, node.right = None, None
        return node

    def push(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.right = node
            node.left = self.tail
            self.tail = node

    def push_new(self, val):
        node = Node(val)
        self.push(node)
        return node

    def to_tail(self, node):
        if self.tail == node:
            return

        self.remove(node)

        self.push(node)

class LRUCache:
    def __init__(self, capacity: int):
        self.ll = DoubleLinkedList()
        self.capacity = capacity
        self.size = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.ll.to_tail(node)
        _, value = node.val
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.size == self.capacity:
                node = self.ll.pop()
                del_key, _ = node.val
                del self.cache[del_key]
                self.size -= 1

            node = self.ll.push_new([key, value])
            self.cache[key] = node
            self.size += 1

        else:
            node = self.cache[key]
            node.val[1] = value
            self.ll.to_tail(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

