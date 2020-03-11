#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        amounts = [(0, nums[0])] # (not_robbed, robbed)

        for i in range(1, len(nums)):
            num = nums[i]
            max_not_robbed = max(amounts[i-1])
            max_robbed = amounts[i-1][0] + num
            amounts.append((max_not_robbed, max_robbed))

        return max(amounts[-1])

# @lc code=end

