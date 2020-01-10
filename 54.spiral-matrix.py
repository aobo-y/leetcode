#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0

        row_min, row_max = 0, m - 1
        col_min, col_max = 0, n -  1

        row, col = 0, 0
        direction = 'right'
        result = []

        while True:
            if row < row_min or row > row_max \
                or col < col_min or col > col_max:
                break

            result.append(matrix[row][col])

            # turn
            if direction == 'right' and col == col_max:
                row_min += 1
                direction = 'down'
            elif direction == 'down' and row == row_max:
                col_max -= 1
                direction = 'left'
            elif direction == 'left' and col == col_min:
                row_max -= 1
                direction = 'up'
            elif direction == 'up' and row == row_min:
                col_min += 1
                direction = 'right'

            if direction == 'right':
                col += 1
            elif direction == 'down':
                row += 1
            elif direction == 'left':
                col -= 1
            elif direction == 'up':
                row -= 1

        return result
# @lc code=end

