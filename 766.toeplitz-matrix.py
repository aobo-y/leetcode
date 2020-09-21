#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row1, row2 in zip(matrix, matrix[1:]):
            if any(v1 != v2 for v1, v2 in zip(row1, row2[1:])):
                return False

        return True

# @lc code=end

