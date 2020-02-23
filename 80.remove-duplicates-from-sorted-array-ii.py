#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        c = 0
        d = None

        for i in nums:
            if d != i:
                d = i
                c = 1
            elif d == i:
                c += 1

            if c <= 2:
                nums[w] = i
                w += 1

        return w

# @lc code=end

