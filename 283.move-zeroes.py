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

        j = -1

        for i, num in enumerate(nums):
            if num == 0 and j == -1:
                j = i
            elif num != 0 and j != -1:
                nums[j] = num
                j = j + 1

        if j != -1:
            for k in range(j, len(nums)):
                if nums[k] != 0:
                    nums[k] = 0

# @lc code=end

