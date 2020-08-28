#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        for n in nums:
            if n > target:
                continue
            dp[n] += 1

        for i in range(target + 1):
            if not dp[i]:
                continue

            for num in nums:
                if i + num > target:
                    continue
                dp[i+num] += dp[i]

        return dp[-1]



# @lc code=end

