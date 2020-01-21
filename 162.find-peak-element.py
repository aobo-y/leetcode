#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def find(start, end):
            i = (start + end) // 2

            if i + 1 < len(nums) and nums[i] < nums[i+1]:
                return find(i+1, end)

            if i - 1 >= 0 and nums[i] < nums[i-1]:
                return find(start, i-1)

            return i

        return find(0, len(nums) - 1)



# @lc code=end

