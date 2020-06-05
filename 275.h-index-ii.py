#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        l, r = 0, len(citations) - 1
        h = 0
        while l <= r:
            i = (l + r) // 2
            n = len(citations) - i
            c = citations[i]

            h = max(min(n, c), h)
            if n > c:
                l = i + 1
            elif n < c:
                r = i - 1
            else:
                break

        return h


# @lc code=end

