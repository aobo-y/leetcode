#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]

            while num and num != i + 1:
                # our of range or already well placed
                if num < 1 or num > len(nums) or nums[num-1] == num:
                    num = 0
                    break

                nums[num-1], num = num, nums[num-1]

            nums[i] = num
            i += 1

        for i in range(len(nums)):
            if not nums[i]:
                return i + 1

        return len(nums) + 1


# @lc code=end

