#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            nums = set()

            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in nums:
                    return False
                nums.add(num)

        for j in range(9):
            nums = set()

            for i in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in nums:
                    return False
                nums.add(num)

        for i in range(3):
            for j in range(3):
                nums = set()

                for k in range(3):
                    for l in range(3):
                        num = board[i*3+k][j*3+l]
                        if num == '.':
                            continue
                        if num in nums:
                            return False
                        nums.add(num)

        return True

# @lc code=end

