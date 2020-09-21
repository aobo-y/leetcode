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

        def inplace_reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        l = len(nums)

        for i in range(l - 2, -1, -1):
            if nums[i] < nums[i+1]:
                inplace_reverse(i + 1, l - 1)
                for j in range(i + 1, l):
                    if  nums[i] < nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                        return

        inplace_reverse(0, l - 1)


# @lc code=end

