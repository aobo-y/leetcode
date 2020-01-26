#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        cache = [[None] * n for _ in range(m)]

        def find_min(row, col):
            if cache[row][col] is not None:
                return cache[row][col]

            if row == m - 1 and col == n - 1:
                next_min_h = 1
            else:
                min_hs = []
                if row < m - 1:
                    min_hs.append(find_min(row + 1, col))
                if col < n - 1:
                    min_hs.append(find_min(row, col + 1))

                next_min_h = min(min_hs)

            min_h = next_min_h - dungeon[row][col]

            if min_h <= 0:
                min_h = 1

            cache[row][col] = min_h

            return min_h

        res = find_min(0, 0)

        return res

# @lc code=end

