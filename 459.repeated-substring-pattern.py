#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        for l in range(1, len(s) // 2 + 1):
            if len(s) % l:
                continue

            if all(s[i] == s[i % l] for i in range(l, len(s))):
                return True

        return False


# @lc code=end

