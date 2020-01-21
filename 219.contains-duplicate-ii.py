#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {}

        for i, num in enumerate(nums):
            if num in cache:
                if i - cache[num] <= k:
                    return True

            cache[num] = i

        return False


# @lc code=end

