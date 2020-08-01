#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'

        res = []
        units = ['Billion', 'Million', 'Thousand', '']

        digits = [None, 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        decimals = [None, None, 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        while num:
            num, r = num // 10 ** 3, num % 10 ** 3

            d1, r = r // 100, r % 100
            d2, r = r // 10, r % 10
            d3 = r

            tokens = []

            if d1:
                tokens += [digits[d1], 'Hundred']

            if d2 == 1:
                tokens.append(tens[d3])
            else:
                if d2:
                    tokens.append(decimals[d2])

                if d3:
                    tokens.append(digits[d3])

            unit = units.pop()
            if tokens:
                if unit:
                    tokens.append(unit)
                res = tokens + res

        return ' '.join(res)


# @lc code=end
