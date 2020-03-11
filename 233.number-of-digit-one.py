#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 0:
            return 0

        digits = [c for c in str(n)]
        count = 0

        for i in range(len(digits)):
            d = int(digits[i])

            left = int(''.join(digits[:i]) or 0) + 1
            right = 10 ** (len(digits) - i - 1)

            if d > 1:
                count += left * right
            elif d == 0:
                count += (left - 1) * right
            elif d == 1:
                count += (left - 1) * right + int(''.join(digits[i+1:]) or 0) + 1


        return count


# @lc code=end

