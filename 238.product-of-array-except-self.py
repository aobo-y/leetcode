#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod, right_prod = 1, 1
        result = [1] * len(nums)

        for i in range(len(nums) - 1):
            left_prod *= nums[i]
            right_prod *= nums[-1-i]

            result[i+1] *= left_prod
            result[-2-i] *= right_prod

        return result


# @lc code=end

