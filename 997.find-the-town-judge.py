#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = defaultdict(set)

        for a, b in trust:
            d[a].add(b)

        nt = [i for i in range(1, N + 1) if i not in d]
        if len(nt) != 1:
            return -1

        if all(nt[0] in a for a in d.values()):
            return nt[0]

        return -1

# @lc code=end

