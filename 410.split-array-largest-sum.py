#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)

        while l < r:
            s = (l + r) // 2

            k = 1
            accum = 0
            for num in nums:
                if accum + num > s:
                    k += 1
                    accum = 0
                accum += num
                if k > m:
                    break

            if k > m:
                l = s + 1
            else:
                r = s

        return l



# @lc code=end

