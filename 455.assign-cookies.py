#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        i, j = 0, 0
        c = 0

        while i < len(g) and j < len(s):
            gv, sv = g[i], s[j]

            if gv <= sv:
                c += 1
                i += 1

            j += 1

        return c

# @lc code=end

