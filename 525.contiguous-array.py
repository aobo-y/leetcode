#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        b_idx = {0: -1}

        balance = 0
        max_l = 0
        for i, num in enumerate(nums):
            if num:
                balance += 1
            else:
                balance -= 1

            if balance not in b_idx:
                b_idx[balance] = i
            else:
                max_l = max(max_l, i - b_idx[balance])
        return max_l

# @lc code=end

