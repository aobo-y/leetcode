#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
from collections import Counter

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        layer = Counter({0: 1})

        for num in nums:
            new_layer = Counter()
            for sign in (1, -1):
                for v, c in layer.items():
                    new_layer[v + sign * num] += c

            layer = new_layer

        return layer[S]

# @lc code=end

