#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # (not_robbed, robbed)
        fst_robbed = (float('-inf'), nums[0])
        fst_not_robbed = (0, float('-inf'))

        for i in range(1, len(nums)):
            num = nums[i]

            fst_robbed = (max(fst_robbed), fst_robbed[0] + num)
            fst_not_robbed = (max(fst_not_robbed), fst_not_robbed[0] + num)

        return max(fst_robbed[0], max(fst_not_robbed))

# @lc code=end

