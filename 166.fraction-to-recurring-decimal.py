#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        s = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        r = s + str(numerator // denominator)
        rem = numerator % denominator

        if not rem:
            return r

        repeat = False
        d = ''
        rems = {}
        while rem and rem not in rems:
            rems[rem] = len(d)
            rem *= 10

            if rem < denominator:
                d += '0'
                continue

            d += str(rem // denominator)
            rem = rem % denominator

        if rem:
            i = rems[rem]
            d = f'{d[:i]}({d[i:]})'

        return r + '.' + d


# @lc code=end

