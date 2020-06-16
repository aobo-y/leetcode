#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda p: p[1])

        counts = 0

        cr = None
        for l, r in pairs:
            if cr is None:
                cr = r
                counts += 1
            elif l > cr:
                cr = r
                counts += 1

        return counts

# @lc code=end

