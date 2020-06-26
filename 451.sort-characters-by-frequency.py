#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)

        sorted_counts = sorted(counts.items(), key=lambda t: t[1], reverse=True)
        return ''.join(k * v for k, v in sorted_counts)


# @lc code=end

