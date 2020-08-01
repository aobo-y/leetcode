#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        unions = {}

        def find_head(pos):
            if pos in unions and pos != unions[pos]:
                head = find_head(unions[pos])
                if head != unions[pos]:
                    unions[pos] = head

                return head
            return pos

        for x, row in enumerate(grid):
            for y, v in enumerate(row):
                if v == '0':
                    continue

                pos = (x, y)
                unions[pos] = pos

                if x != 0 and grid[x-1][y] == '1':
                    head = find_head((x - 1, y))
                    unions[head] = pos
                if y != 0 and grid[x][y-1] == '1':
                    head = find_head((x, y - 1))
                    unions[head] = pos
        # for pos, v in unions.items():
        #     print(pos, v)
        return sum(1 for pos, v in unions.items() if pos == v)






# @lc code=end

