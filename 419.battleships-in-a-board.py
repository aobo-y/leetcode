#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        c = 0
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == '.':
                    continue

                if i > 0 and board[i-1][j] == 'X':
                    continue

                if j > 0 and row[j-1] == 'X':
                    continue

                c += 1

        return c

# @lc code=end

