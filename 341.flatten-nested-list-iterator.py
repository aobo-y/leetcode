#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.kl_pairs = [(-1, nestedList)]
        self.find_next()

    def find_next(self):
        while self.kl_pairs:
            k, l = self.kl_pairs.pop()

            if k == len(l) - 1:
                continue

            self.kl_pairs.append((k + 1, l))
            val = l[k + 1]

            if not val.isInteger():
                l = val.getList()
                self.kl_pairs.append((-1, l))
            else:
                break

    def next(self) -> int:
        k, l = self.kl_pairs[-1]
        self.find_next()

        return l[k]


    def hasNext(self) -> bool:
        return bool(self.kl_pairs)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

