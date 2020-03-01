#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        sizes = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    k = 1
                    while i - k >= 0 and matrix[i-k][j] == '1' \
                        and j - k >= 0 and matrix[i][j-k] == '1' \
                        and sizes[i-1][j-1] >= k:
                        k += 1

                    sizes[i][j] = k

        return max([max(row) for row in sizes], default=0) ** 2

# @lc code=end

