#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = 0

        for i, num in enumerate(nums):
            if num != 0:
                if j != i:
                    nums[j] = num
                j = j + 1

        for k in range(j, len(nums)):
            nums[k] = 0

# @lc code=end

