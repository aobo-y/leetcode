#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if not dividend:
            return 0

        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        MAX = 2 ** 30 - 1 + 2 ** 30

        div, c = divisor, 1
        r = 0
        while dividend >= divisor:
            while (div << 1) < dividend and c < 31:
                div <<= 1
                c <<= 1
            while dividend < div:
                div >>= 1
                c >>= 1

            dividend -= div

            if c > MAX - r:
                return MAX if sign == 1 else -MAX - 1
            r += c

        return r * sign


# @lc code=end

