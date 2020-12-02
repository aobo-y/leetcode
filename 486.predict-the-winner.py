#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#

# @lc code=start
from functools import lru_cache
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def highest_score(l, r):
            if l == r:
                return nums[l], 0

            lp2, lp1 = highest_score(l + 1, r)
            lp1 += nums[l]

            rp2, rp1 = highest_score(l, r - 1)
            rp1 += nums[r]

            return (lp1, lp2) if lp1 > rp1 else (rp1, rp2)

        p1, p2 = highest_score(0, len(nums) - 1)
        return p1 >= p2
# @lc code=end

