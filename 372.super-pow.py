#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a %= 1337 # avoid too large a

        def backward():
            rem = 1

            for n in b[::-1]:
                rem *= a ** n % 1337
                rem %= 1337
                a = a ** 10 % 1337

            return rem

        def forward():
            rem = 1

            for n in b:
                rem = ((rem ** 10 % 1337) * (a ** n % 1337)) % 1337

            return rem

        return forward()

# @lc code=end

