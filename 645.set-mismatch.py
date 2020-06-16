#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        res = [None, None]
        while i < len(nums):
            num = nums[i]
            while num is not None and num - 1 != i:
                if nums[num - 1] == num:
                    res[0] = num
                    num = None
                else:
                    nums[num - 1], num = num, nums[num - 1]

            nums[i] = num
            if num is None:
                res[1] = i + 1
            i += 1
        return res

# @lc code=end

