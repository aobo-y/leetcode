#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, string: str) -> int:
        v = 0
        sign = None

        for c in string.lstrip():
            if not sign and (c == '+' or c == '-'):
                sign = c
                continue

            if not c.isdigit():
                break

            if not sign:
                sign = '+'

            d = int(c)
            v = v * 10 + d

        if sign == '-':
            v = -v

        if v > 2 ** 31 - 1:
            v = 2 ** 31 - 1
        elif v < - (2 ** 31):
            v = - (2 ** 31)

        return v

# @lc code=end

