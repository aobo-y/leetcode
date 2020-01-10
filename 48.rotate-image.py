#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for start_idx in range(n):
            end_idx = n - start_idx - 1
            if start_idx >= end_idx:
                return

            row_idx = start_idx
            for col_idx in range(start_idx, end_idx):
                tmp = matrix[row_idx][col_idx]

                for _ in range(4):
                    matrix[col_idx][n - row_idx - 1], tmp = tmp, matrix[col_idx][n - row_idx - 1]

                    row_idx, col_idx = col_idx, n - row_idx - 1


        return


# @lc code=end

