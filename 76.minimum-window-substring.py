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

        i = 0
        m = 0
        min_sub = ''

        for i in range(len(s)):
            c = s[i]

            if c not in needs:
                continue

            if needs[c] > 0:
                pending -= 1
            needs[c] -= 1

            if not pending:
                while True:
                    mc = s[m]
                    if mc in needs:
                        if needs[mc] == 0:
                            break
                        else:
                            needs[mc] += 1

                    m += 1

                length = i - m + 1
                if not min_sub or length < len(min_sub):
                    min_sub = s[m:i+1]

        return min_sub



# @lc code=end

