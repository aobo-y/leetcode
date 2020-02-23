#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        nums = [1]

        for i, c in enumerate(s):
            n = 0 if c == '0' else nums[-1]
            if i > 0 and s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                n += nums[-2]
            nums.append(n)

        return nums[-1]




# @lc code=end

