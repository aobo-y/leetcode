#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        a = 1
        i, j = 0, 0
        while n > 0:
            if n == 1:
                matrix[i][j] = a
            else:
                for k in range(n - 1):
                    matrix[i][j+k] = a
                    a += 1

                for k in range(n - 1):
                    matrix[i+k][j+n-1] = a
                    a += 1

                for k in range(n - 1):
                    matrix[i+n-1][j+n-1-k] = a
                    a += 1

                for k in range(n - 1):
                    matrix[i+n-1-k][j] = a
                    a += 1

            n -= 2
            i += 1
            j += 1

        return matrix

# @lc code=end

