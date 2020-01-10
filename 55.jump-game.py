#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        min_idx, max_idx = 0, 0
        last_idx = len(nums) - 1

        while min_idx <= max_idx:
            new_max = max_idx

            for i in range(min_idx, max_idx + 1):
                if i + nums[i] > new_max:
                    new_max = i + nums[i]

            if new_max >= last_idx:
                return True

            min_idx, max_idx = max_idx + 1, new_max


        return False

# @lc code=end

