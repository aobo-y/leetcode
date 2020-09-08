#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def window():
            max_sum = float('-inf')

            start_idx = 0
            sum_ = 0
            for end_idx, num in enumerate(nums):
                if sum_ < 0:
                    start_idx = end_idx
                    sum_ = 0

                sum_ += num

                if sum_ > max_sum:
                    max_sum = sum_

            return max_sum

        def prefix():
            max_sum = float('-inf')
            min_prefix = 0
            presum = 0

            for num in nums:
                presum += num
                max_sum = max(max_sum, presum - min_prefix)
                min_prefix = min(min_prefix, presum)

            return max_sum

        return prefix()


# @lc code=end

