#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_set, col_set = set(), set()

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0

# @lc code=end

