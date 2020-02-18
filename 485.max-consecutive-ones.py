#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_c = 0
        s = None
        for i, v in enumerate(nums + [0]):
            if v and s is None:
                s = i
            elif not v and s is not None:
                if i - s > max_c:
                    max_c = i - s
                s = None
        return max_c

# @lc code=end

