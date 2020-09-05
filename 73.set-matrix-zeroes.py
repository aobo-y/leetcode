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

        def space_mn():
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

        def space_1():
            row0, col0 = 1, 1
            for i, row in enumerate(matrix):
                for j, val in enumerate(row):
                    if val:
                        continue

                    if not i:
                        row0 = 0
                    else:
                        matrix[i][0] = 0

                    if not j:
                        col0 = 0
                    else:
                        matrix[0][j] = 0

            for i in range(len(matrix) - 1, -1, -1):
                row = matrix[i]
                for j in range(len(row) - 1, -1, -1):
                    if not i:
                        if not row0:
                            row[j] = 0
                    elif not matrix[i][0]:
                        row[j] = 0


                    if not j:
                        if not col0:
                            row[j] = 0
                    elif not matrix[0][j]:
                        row[j] = 0

            return matrix

        return space_1()


# @lc code=end

