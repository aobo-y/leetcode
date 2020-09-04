#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {'a': 0, 'b': 0, 'c': 0}
        r = 0

        i = 0
        for j, c in enumerate(s):
            d[c] += 1
            if not (d['a'] and d['b'] and d['c']):
                continue

            while d[s[i]] > 1:
                d[s[i]] -= 1
                i += 1

            r += i + 1

        return r

# @lc code=end

