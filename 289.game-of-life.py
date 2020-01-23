#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0]) if board else 0

        def find_live_n(i, j):
            live_count = 0

            rows, cols = [i], [j]
            if i > 0:
                rows.append(i - 1)
            if i < m - 1:
                rows.append(i + 1)
            if j > 0:
                cols.append(j - 1)
            if j < n - 1:
                cols.append(j + 1)

            for row in rows:
                for col in cols:
                    if row == i and col == j:
                        continue

                    if board[row][col] > 0:
                        live_count += 1

            return live_count

        for i in range(m):
            for j in range(n):
                count = find_live_n(i, j)

                if (count < 2 or count > 3) and board[i][j] == 1:
                    board[i][j] = 2
                elif count == 3 and board[i][j] == 0:
                    board[i][j] = -1

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1



# @lc code=end

