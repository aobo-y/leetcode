#
# @lc app=leetcode id=639 lang=python3
#
# [639] Decode Ways II
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        dp_1, dp_2 = 1, 0

        for i, c in enumerate(s):
            dp = 0
            if c != '*':
                if c != '0':
                    dp += dp_1
            else:
                dp += 9 * dp_1

            if i > 0 and s[i - 1] in ['*', '1']:
                if c != '*':
                    dp += dp_2
                else:
                    dp += 9 * dp_2

            if i > 0 and s[i - 1] in ['*', '2']:
                if c != '*':
                    if c <= '6':
                        dp += dp_2
                else:
                    dp += 6 * dp_2

            dp_1, dp_2 = dp, dp_1

        return dp_1 % (7 + 10 ** 9)

# @lc code=end

