#
# @lc app=leetcode id=1428 lang=python3
#
# [1428] Leftmost Column with at Least a One
#

# @lc code=start
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()

        def left_col(i, r):  # row idx & right idx
            l = 0

            while l < r:
                k = (l + r) // 2
                if binaryMatrix.get(i, k):
                    r = k
                else:
                    l = k + 1

            return l if binaryMatrix.get(i, l) else -1

        r = n
        for i in range(m):
            nr = left_col(i, r - 1)
            if nr != -1:
                r = nr

        return r if r != n else -1
# @lc code=end

