#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            num = nums[i]
            while num and i != num - 1:
                if num == nums[num - 1]:
                    res.append(num)
                    nums[i] = None
                else:
                    nums[num - 1], nums[i] = num, nums[num - 1]

                num = nums[i]
        return res




# @lc code=end

