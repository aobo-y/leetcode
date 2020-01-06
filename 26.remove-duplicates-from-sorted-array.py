#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_idx = 0
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            if i != write_idx:
                nums[write_idx] = num

            write_idx += 1

        return write_idx

# @lc code=end

