#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        r = []

        i = 1
        b = 0

        while len(num1) >= i or len(num2) >= i or b:
            x = num1[-i] if len(num1) >= i else 0
            y = num2[-i] if len(num2) >= i else 0
            v = int(x) + int(y) + b
            v, b = v % 10, v // 10
            r.append(v)
            i += 1

        return ''.join([str(v) for v  in r[::-1]])


# @lc code=end

