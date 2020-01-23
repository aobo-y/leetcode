#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.node = None

    def book(self, start: int, end: int) -> bool:
        if not self.node:
            self.node = Node(start, end)
            return True

        node = self.node
        while node:
            if start >= node.end:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(start, end)
                    return True

            elif end <= node.start:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(start, end)
                    return True

            else:
                return False



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

