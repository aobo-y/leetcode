#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row_vals = defaultdict(set)
        col_vals = defaultdict(set)
        grid_vals = defaultdict(set)

        cells = []

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    cells.append([i, j])
                    continue

                num = int(num)
                row_vals[i].add(num)
                col_vals[j].add(num)
                grid_vals[(i // 3) * 3 + j // 3].add(num)

        def dfs(k):
            if k == len(cells):
                return True

            i, j = cells[k]

            for v in range(1, 10):
                if v in row_vals[i] or v in col_vals[j] or v in grid_vals[(i // 3) * 3 + j // 3]:
                    continue

                row_vals[i].add(v)
                col_vals[j].add(v)
                grid_vals[(i // 3) * 3 + j // 3].add(v)

                res = dfs(k + 1)

                if res:
                    board[i][j] = str(v)
                    return True

                row_vals[i].remove(v)
                col_vals[j].remove(v)
                grid_vals[(i // 3) * 3 + j // 3].remove(v)

            return False

        dfs(0)
        return


# @lc code=end

