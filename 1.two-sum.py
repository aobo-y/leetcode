#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_idx_dict:
                return [num_idx_dict[complement], i]

            num_idx_dict[num] = i

        return None

# @lc code=end

