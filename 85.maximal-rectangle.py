#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n_row, n_col = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        cache = [[None] * n_col for _ in range(n_row)]

        max_rect = 0

        def find(row, col):
            if matrix[row][col] == '0':
                return [0, 0]

            if cache[row][col] is None:
                w, h = 1, 1
                if row < n_row - 1 and matrix[row + 1][col] != '0':
                    h += find(row + 1, col)[1]

                if col < n_col - 1 and matrix[row][col + 1] != '0':
                    w += find(row, col + 1)[0]

                cache[row][col] = [w, h]

            return cache[row][col]

        for i in range(n_row):
            for j in range(n_col):
                if matrix[i][j] == '0':
                    continue

                w, h = find(i, j)

                min_w = w

                if min_w * 1 > max_rect:
                    max_rect = min_w

                for k in range(1, h):
                    w2, _ = find(i + k, j)
                    min_w = min(min_w, w2)
                    area = min_w * (k + 1)

                    if area > max_rect:
                        max_rect = area

        return max_rect

# @lc code=end

