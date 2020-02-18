#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = []
        carry = 0

        for i, d1 in enumerate(num1[::-1]):
            d1 = int(d1)
            for j, d2 in enumerate(num2[::-1]):
                d2 = int(d2)
                val = d1 * d2 + carry

                k = i + j
                if len(res) <= k:
                    res.append(0)

                val += res[k]
                carry = val // 10
                res[k] = val % 10
            res.append(carry) # carry wont exceed 9
            carry = 0

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return ''.join([str(d) for d in res[::-1]])


# @lc code=end

