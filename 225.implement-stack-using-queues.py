#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack = deque([x, self.stack])

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        x = self.stack.popleft()
        self.stack = self.stack.popleft()
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.stack)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

