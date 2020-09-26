#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        u = {(r, c): (r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v}

        def head(p):
            if u[p] == p:
                return p
            u[p] = head(u[p])
            return u[p]

        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if not v:
                    continue

                for nr, nc in [(r - 1, c), (r, c - 1)]:
                    if nr >= 0 and nc >= 0 and grid[nr][nc]:
                        u[head((r, c))] = head((nr, nc))

        islands = {p: 0 for p, h in u.items() if p == h}
        for p in u:
            islands[head(p)] += 1

        max_size = max(islands.values(), default=0)
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v:
                    continue

                connected = set()
                for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                    if 0 <= nr < len(grid) and 0 <= nc < len(row) and grid[nr][nc]:
                        connected.add(head((nr, nc)))

                size = 1 + sum(islands[i] for i in connected)
                max_size = max(max_size, size)

        return max_size


# @lc code=end

