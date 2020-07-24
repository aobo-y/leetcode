#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#

# @lc code=start
class Solution:
    from collections import Counter
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter([a + 1 for a in answers])
        s = 0
        for v, c in counts.items():
            s += ((c - 1) // v + 1) * v

        return s

# @lc code=end

