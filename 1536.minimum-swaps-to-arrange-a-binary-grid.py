#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#

# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        counts = [0] * n
        for i, row in enumerate(grid):
            c = 0
            for j in range(n - 1, -1, -1):
                if row[j] != 0:
                    break
                c += 1
            counts[i] = c

        res = 0
        for i in range(n):
            req = n - 1 - i
            c = 0
            j = i
            while counts[j] < req:
                j += 1
                if j >= n:
                    return -1

            res += j - i
            counts[i], counts[i+1:j+1] = counts[j], counts[i:j]

        return res


# @lc code=end

