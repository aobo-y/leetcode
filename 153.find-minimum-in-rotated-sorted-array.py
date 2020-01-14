#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find(start, end):
            if end == start:
                return nums[start]

            idx = (start + end) // 2

            val = nums[idx]

            if nums[end] > nums[start]:
                return nums[start]

            elif val > nums[end]:
                return find(idx + 1, end)

            elif val < nums[start]:
                return find(start + 1, idx)

        return find(0, len(nums) - 1)



# @lc code=end

