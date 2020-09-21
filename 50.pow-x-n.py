#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x

        res = 1 if not n % 2 else x

        p = self.myPow(x, n // 2)
        res *= p * p

        return res

# @lc code=end

