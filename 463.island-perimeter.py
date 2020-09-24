#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if not v:
                    continue

                p += 2
                p += 1 if not i or not grid[i-1][j] else -1
                p += 1 if not j or not grid[i][j-1] else -1

        return p

# @lc code=end

