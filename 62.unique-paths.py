#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cache = [[-1] * n for _ in range(m)]

        # def find_paths(row, column):
        #     if cache[row][column] == -1:
        #         if row == m - 1 or column == n - 1:
        #             cache[row][column] = 1
        #         else:
        #             paths = 0
        #             if row < m - 1:
        #                 paths += find_paths(row + 1, column)
        #             if column < n - 1:
        #                 paths += find_paths(row, column + 1)

        #             cache[row][column] = paths

        #     return cache[row][column]

        # return find_paths(0, 0)

        steps = (m - 1) + (n - 1)

        small = min(m - 1, n - 1)

        norm, denorm = 1, 1
        for i in range(small):
            norm *= (steps - i)
            denorm *= (small - i)

        return int(norm / denorm)



# @lc code=end

