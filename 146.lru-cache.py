#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head

    def pop_head(self):
        if self.head.right == self.tail:
            return None

        node = self.head.right
        self.remove(node)
        return node

    def push_tail(self, val):
        node = Node(val)
        self.append(node)
        return node

    def remove(self, node):
        node.left.right, node.right.left = node.right, node.left

    def append(self, node):
        node.left, node.right = self.tail.left, self.tail
        self.tail.left.right = node
        self.tail.left = node

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
        self.ll.remove(node)
        self.ll.append(node)
        _, value = node.val
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.size == self.capacity:
                node = self.ll.pop_head()
                del_key, _ = node.val
                del self.cache[del_key]
                self.size -= 1

            node = self.ll.push_tail([key, value])
            self.cache[key] = node
            self.size += 1

        else:
            node = self.cache[key]
            node.val[1] = value
            self.ll.remove(node)
            self.ll.append(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

