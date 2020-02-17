#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sort_c = sorted(citations, reverse=True)

        for i, c in enumerate(sort_c):
            if i + 1 > c:
                return i

        return len(sort_c)


# @lc code=end

