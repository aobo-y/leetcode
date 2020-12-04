#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counts = Counter(moves)
        return counts['L'] == counts['R'] and counts['U'] == counts['D']

# @lc code=end

