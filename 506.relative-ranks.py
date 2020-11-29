#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        ranks = sorted([(n, i) for i, n in enumerate(nums)], reverse=True)
        res = [None] * len(nums)
        for i, (_, idx) in enumerate(ranks):
            if not i:
                res[idx] = 'Gold Medal'
            elif i == 1:
                res[idx] = 'Silver Medal'
            elif i == 2:
                res[idx] = 'Bronze Medal'
            else:
                res[idx] = str(i + 1)

        return res

# @lc code=end

