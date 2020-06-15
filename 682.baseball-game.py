#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []
        for op in ops:
            if op == '+':
                points.append(points[-2] + points[-1])
            elif op == 'D':
                points.append(2 * points[-1])
            elif op == 'C':
                points.pop()
            else:
                points.append(int(op))
        return sum(points)

# @lc code=end

