#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_len = 0

        val = 0
        i = 0
        for j, num in enumerate(nums):
            val += num

            if val >= s:
                while i < j:
                    if val - nums[i] < s:
                        break

                    val -= nums[i]
                    i += 1

                length = j - i + 1
                if min_len == 0 or length < min_len:
                    min_len = length

        return min_len


# @lc code=end

