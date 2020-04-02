#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        max_buffer = [None] * len(nums)
        start, end = 0, 0

        res = []

        for i, num in enumerate(nums):
            # remove left item
            if i >= k and nums[i-k] == max_buffer[start]:
                start += 1

            # add right item
            l, r = start, end
            while l < r:
                idx = (r + l) // 2
                val = max_buffer[idx]
                if num > val:
                    r = idx
                elif num <= val:
                    l = idx + 1

            if max_buffer[l] is not None and max_buffer[l] >= num:
                l += 1
            max_buffer[l] = num
            end = l

            if i >= k - 1:
                res.append(max_buffer[start])

        return res



# @lc code=end

