#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        w = 0

        for r, num in enumerate(nums):
            if num != val:
                if r != w:
                    nums[w] = num
                w += 1

        del nums[w:]
        return w



# @lc code=end

