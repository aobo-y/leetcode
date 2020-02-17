#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'

        for i in range(2, n + 1):
            ns = ''
            f = 0
            for sc in s:
                if f == 0 or c == sc:
                    f += 1
                else:
                    ns += str(f) + c
                    f = 1
                c = sc
            ns += str(f) + c
            s = ns

        return s


# @lc code=end

