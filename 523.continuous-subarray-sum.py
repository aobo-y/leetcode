#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum_r = {0: -1}  # presum's remainders: index

        r = 0
        for i, n in enumerate(nums):
            r = n + r
            if k:
                r %= k

            if r not in presum_r:
                presum_r[r] = i
            elif i - presum_r[r] == 1:
                continue
            else:
                return True
        return False


# @lc code=end

