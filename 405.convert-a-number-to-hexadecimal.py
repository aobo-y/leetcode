#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if not num:
            return '0'
        if num < 0:
            return self.toHex(2 ** 31 + num + 2 ** 31)

        r = []

        while num:
            d = num % 16
            num //= 16

            c = chr(ord('a') + d - 10) if d > 9 else str(d)

            r.append(c)

        return ''.join(r[::-1])



# @lc code=end

