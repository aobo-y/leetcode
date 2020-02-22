#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(row, queens, col_mask=set(), forward_mask=set(), backward_mask=set()):
            if len(queens) == n:
                return [[
                    '.' * q_col + 'Q' + '.' * (n - q_col - 1)
                    for _, q_col in queens
                ]]

            res = []
            for col in range(n):
                forward_diag = row + col
                backward_diag = n - 1 - row + col

                if col in col_mask \
                    or forward_diag in forward_mask \
                    or backward_diag in backward_mask:
                    continue

                queens.append((row, col))
                col_mask.add(col)
                forward_mask.add(forward_diag)
                backward_mask.add(backward_diag)

                res += solve(row + 1, queens, col_mask, forward_mask, backward_mask)

                queens.pop()
                col_mask.remove(col)
                forward_mask.remove(forward_diag)
                backward_mask.remove(backward_diag)

            return res

        return solve(0, [])


# @lc code=end

