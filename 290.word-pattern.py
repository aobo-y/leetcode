#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        tokens = str.split(' ')
        if len(pattern) != len(tokens):
            return False

        c2t, t2c = {}, {}
        for c, token in zip(pattern, tokens):
            if c not in c2t:
                c2t[c] = token
            if token not in t2c:
                t2c[token] = c

            if t2c[token] != c or c2t[c] != token:
                return False

        return True


# @lc code=end

