#
# @lc app=leetcode id=385 lang=python3
#
# [385] Mini Parser
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        num = None
        sign = 1
        res = None
        stack = []

        for l in s:
            if l in ',]' and num is not None:
                res.add(NestedInteger(sign * num))
                num = None
                sign = 1

            if l == '[':
                new_list = NestedInteger()
                if res:
                    stack.append(res)
                    res.add(new_list)

                res = new_list

            elif l == ']' and stack:
                res = stack.pop()

            elif l.isdigit():
                if num is None:
                    num = int(l)
                else:
                    num = num * 10 + int(l)
            elif l == '-':
                sign = -1



        return res

# @lc code=end

