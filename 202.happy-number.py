#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n not in s and n != 1:
            s.add(n)

            v = 0

            while n != 0:
                n, d = n // 10, n % 10
                v += d ** 2

            n = v


        return n == 1

# @lc code=end

