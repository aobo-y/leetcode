#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        next_row_mins = [_ for _ in triangle[-1]]

        # when length is 1, loop will be skipped
        for i in range(len(triangle) - 2, -1, -1):
            row = triangle[i]

            for j, v in enumerate(row):
                left, right = next_row_mins[j], next_row_mins[j + 1]
                next_row_mins[j] = min(left, right) + v

        return next_row_mins[0]




# @lc code=end

