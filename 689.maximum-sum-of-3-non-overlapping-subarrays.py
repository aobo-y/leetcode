#
# @lc app=leetcode id=689 lang=python3
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#

# @lc code=start
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        subary_sums = []
        s = sum(nums[:k-1])
        for i in range(k - 1, len(nums)):
            s += nums[i]
            if i - k >= 0:
                s -= nums[i-k]
            subary_sums.append(s)

        dp = []
        for i in range(len(nums) - k + 1):
            subary_sum = subary_sums[i]
            state = {1: (subary_sum, [i])}

            l = i - k
            if l >= 0:
                prev_state = dp[l]
                for t, s in prev_state.items():
                    if t != 3:
                        val, ind = s
                        state[t+1] = (val + subary_sum, [*ind, i])

            if dp:
                last_state = dp[-1]
                for t, s in last_state.items():
                    if s[0] >= state[t][0]:
                        state[t] = s

            dp.append(state)

        return dp[-1][3][1]


# @lc code=end

