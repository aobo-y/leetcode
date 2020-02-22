#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x = -x
            neg = True

        r = 0
        while x:
            r *= 10
            r += (x % 10)
            x //= 10

        if neg:
            r = -r

        if r > 2 ** 31 - 1 or r < - (2 ** 31):
            r = 0

        return r


# @lc code=end

