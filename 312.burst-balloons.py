#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}

        def max_subary(i, j):
            if i > j:
                return 0

            key = (i, j)
            if key in cache:
                return cache[key]

            m = float('-inf')
            for k in range(i, j + 1):
                c = nums[k] * (nums[i-1] if i > 0 else 1) * (nums[j+1] if j < len(nums) - 1 else 1)

                m = max(m, c + max_subary(i, k - 1) + max_subary(k + 1, j))

            cache[key] = m
            return m

        return max_subary(0, len(nums) - 1)


# @lc code=end

