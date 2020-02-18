#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0]) if matrix else 0

        def split_matrix(row_l, row_r, col_l, col_r):
            if row_l > row_r or col_l > col_r:
                return False

            row_i = (row_l + row_r) // 2
            col_i = (col_l + col_r) // 2

            val = matrix[row_i][col_i]

            if val > target:
                return split_matrix(row_l, row_i - 1, col_l, col_i - 1) \
                    or split_matrix(row_i, row_r, col_l, col_i - 1) \
                    or split_matrix(row_l, row_i - 1, col_i, col_r)
            elif val < target:
                return split_matrix(row_i + 1, row_r, col_i + 1, col_r) \
                    or split_matrix(row_l, row_i, col_i + 1, col_r) \
                    or split_matrix(row_i + 1, row_r, col_l, col_i)
            else:
                return True



        def right_corner(r, c):
            if r >= m or c >= n or r < 0 or c < 0:
                return False

            val = matrix[r][c]

            if val > target:
                return right_corner(r, c - 1)
            elif val < target:
                return right_corner(r + 1, c)
            return True

        return right_corner(0, n - 1)

# @lc code=end

