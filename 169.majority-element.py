#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        threshold = len(nums) // 2

        for num in nums:
            if num not in counts:
                counts[num] = 0

            counts[num] += 1
            if counts[num] > threshold:
                return num


# @lc code=end

