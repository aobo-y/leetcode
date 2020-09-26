#
# @lc app=leetcode id=1424 lang=python3
#
# [1424] Diagonal Traverse II
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n_row, n_col = len(nums), max(len(row) for row in nums)
        n_dia = n_row + n_col - 1

        res = [[] for _ in range(n_dia)]
        for r in range(n_row - 1, -1, -1):
            for c, v in enumerate(nums[r]):
                res[r+c].append(v)

        return [v for dia in res for v in dia]

# @lc code=end

