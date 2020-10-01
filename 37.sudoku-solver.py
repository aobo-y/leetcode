#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row_vals = [[False] * 10 for _ in range(9)]
        col_vals = [[False] * 10 for _ in range(9)]
        grid_vals = [[False] * 10 for _ in range(9)]

        grid_idx = lambda i, j: (i // 3) * 3 + j // 3

        cells = []

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    cells.append([i, j])
                    continue

                num = int(num)
                row_vals[i][num] = True
                col_vals[j][num] = True
                grid_vals[grid_idx(i, j)][num] = True

        def dfs(k):
            if k == len(cells):
                return True

            i, j = cells[k]

            for v in range(1, 10):
                if row_vals[i][v] or col_vals[j][v] or grid_vals[grid_idx(i, j)][v]:
                    continue

                row_vals[i][v] = True
                col_vals[j][v] = True
                grid_vals[grid_idx(i, j)][v] = True

                if dfs(k + 1):
                    board[i][j] = str(v)
                    return True

                row_vals[i][v] = False
                col_vals[j][v] = False
                grid_vals[grid_idx(i, j)][v] = False

            return False

        dfs(0)
        return


# @lc code=end

