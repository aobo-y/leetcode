#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[None] * n for _ in range(m)]

        layer = {
            (i, j)
            for i, row in enumerate(matrix)
            for j, v in enumerate(row)
            if not v
        }
        d = 0

        while layer:
            for i, j in layer:
                res[i][j] = d

            layer = {
                (ni, nj)
                for i, j in layer
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                if 0 <= ni < m and 0 <= nj < n and res[ni][nj] is None
            }

            d += 1

        return res


# @lc code=end

