#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = Counter([0])
        s = 0
        c = 0
        for n in nums:
            s += n
            c += prefix[s - k]
            prefix[s] += 1

        return c

# @lc code=end

