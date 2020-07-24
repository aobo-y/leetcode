#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[None] * c for _ in range(r)]

        i = 0
        for row in nums:
            for n in row:
                res[i // c][i % c] = n
                i += 1

        if i != r * c:
            return nums

        return res

# @lc code=end

