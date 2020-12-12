#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints[:k])
        r = s
        for i in range(k):
            s = s - cardPoints[k-i-1] + cardPoints[-i-1]
            r = max(r, s)

        return r

# @lc code=end

