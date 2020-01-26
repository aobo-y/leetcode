#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) if matrix else 0

        if m == 0 or n == 0:
            return False

        def keep_matrix():
            row_start, row_end = 0, m - 1

            while row_start <= row_end:
                row_idx = (row_start + row_end) // 2

                row_min, row_max = matrix[row_idx][0], matrix[row_idx][-1]

                if target < row_min:
                    row_end = row_idx - 1
                elif target > row_max:
                    row_start = row_idx + 1
                else:
                    col_start, col_end = 0, n - 1

                    while col_start <= col_end:
                        col_idx = (col_start + col_end) // 2

                        v = matrix[row_idx][col_idx]

                        if target < v:
                            col_end = col_idx - 1
                        elif target > v:
                            col_start = col_idx + 1
                        else:
                            return True

                    return False

            return False


        def flatten():
            l = m * n
            start, end = 0, l - 1

            while start <= end:
                idx = (start + end) // 2
                v = matrix[idx // n][idx % n]

                if target < v:
                    end = idx - 1
                elif target > v:
                    start = idx + 1
                else:
                    return True

            return False

        return flatten() # keep_matrix()



# @lc code=end

