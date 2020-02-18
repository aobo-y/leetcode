#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        for i in range(max(len(a), len(b))):
            ad = int(a[-i-1]) if i < len(a) else 0
            bd = int(b[-i-1]) if i < len(b) else 0

            val = ad + bd + carry
            carry = val // 2
            res.append(val % 2)
        if carry:
            res.append(carry)
        return ''.join([str(d) for d in res[::-1]])

# @lc code=end

