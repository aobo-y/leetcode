#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        cs = Counter(S)

        cs = sorted(cs.items(), key=lambda t: t[1], reverse=True)
        max_c = cs[0][1]

        if max_c > (len(S) + 1) // 2:
            return ''

        s_grps = [[] for _ in range(max_c)]

        i = 0
        for c, count in cs:
            for _ in range(count):
                s_grps[i % max_c].append(c)
                i += 1

        return ''.join(''.join(grp) for grp in s_grps)


# @lc code=end

