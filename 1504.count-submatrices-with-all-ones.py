#
# @lc app=leetcode id=1504 lang=python3
#
# [1504] Count Submatrices With All Ones
#

# @lc code=start
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        len_count = [[0] * n for _ in range(m)]
        for i in range(m):
            l = 0  # continuous length
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 1:
                    l += 1
                else:
                    l = 0

                len_count[i][j] = l

        r = 0
        for i in range(m):
            for j in range(n):
                v = mat[i][j]
                if not v:
                    continue

                ii = i
                l = float('inf')
                while ii < m and mat[ii][j] == 1:
                    l = min(l, len_count[ii][j])
                    r += l
                    ii += 1

        return r

# @lc code=end

