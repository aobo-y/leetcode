#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        self.cache = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.cache[i][j] += matrix[i][j] \
                    + (self.cache[i-1][j] if i else 0) \
                    + (self.cache[i][j-1] if j else 0) \
                    - (self.cache[i-1][j-1] if i and j else 0)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cache[row2][col2] \
            - (self.cache[row2][col1-1] if col1 else 0) \
            - (self.cache[row1-1][col2] if row1 else 0) \
            + (self.cache[row1-1][col1-1] if row1 and col1 else 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

