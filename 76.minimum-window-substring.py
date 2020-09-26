#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pending = len(t)
        needs = Counter(t)

        m = 0
        min_sub = ''

        for i, c in enumerate(s):
            if c not in needs:
                continue

            if needs[c] > 0:
                pending -= 1
            needs[c] -= 1

            while s[m] not in needs or needs[s[m]] < 0:
                if s[m] in needs:
                    needs[s[m]] += 1
                m += 1

            if not pending and (not min_sub or i - m + 1 < len(min_sub)):
                min_sub = s[m:i+1]

        return min_sub


# @lc code=end

