#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return bool(n % 4)

        # DP
        ary = [None, True, True, True]

        while len(ary) <= n:
            i = len(ary)
            ary.append(not ary[i-1] or not ary[i-2] or not ary[i-3])

        return ary[n]



# @lc code=end

