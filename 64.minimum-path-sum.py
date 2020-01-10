#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = [[-1] * n for _ in range(m)]

        def find_min(row, col):
            if cache[row][col] == -1:
                if row == m - 1 and col == n - 1:
                    cache[row][col] = grid[row][col]
                else:
                    paths = []
                    if row < m - 1:
                        paths.append(find_min(row + 1, col))
                    if col < n - 1:
                        paths.append(find_min(row, col + 1))

                    cache[row][col] = grid[row][col] + min(paths)

            return cache[row][col]

        return find_min(0, 0)

# @lc code=end

