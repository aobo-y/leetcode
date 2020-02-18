#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 1]
        for i in range(2, n + 1):
            ways.append(ways[-1] + ways[-2])
        return ways[-1]

# @lc code=end

