#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def min_steps(p1, p2):
            if p1 == len(word1):
                return len(word2) - p2
            if p2 == len(word2):
                return len(word1) - p1

            if word1[p1] == word2[p2]:
                return min_steps(p1 + 1, p2 + 1)

            return 1 + min(min_steps(p1 + 1, p2), min_steps(p1, p2 + 1))

        return min_steps(0, 0)
# @lc code=end

