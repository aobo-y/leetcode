#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        max_num = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < max_num:
                nums[i + 1:] = nums[:i:-1]
                for j in range(i + 1, len(nums)):
                    if  nums[i] < nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                        return nums

            else:
                max_num = nums[i]

        nums[:] = nums[::-1]
        return nums


# @lc code=end

