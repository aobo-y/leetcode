#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
from collections import Counter

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # handle decimal precision
        def gcd(x, y):
            z = x % y
            if z == 0:
                return y
            else:
                return gcd(y, z)

        max_n = 0
        for i in range(len(points)): # till the end instead of len-1 the case of single point
            slope_counts = Counter()
            n_source_points = 1 # test cases contain duplicate points...
            for j in range(i + 1, len(points)):
                ip, jp = points[i], points[j]
                dx, dy = jp[0] - ip[0], jp[1] - ip[1]
                if dx == 0 and dy == 0:
                    n_source_points += 1
                    continue

                if dy == 0:
                    slope = 'inf'
                else:
                    d = gcd(dx, dy)
                    slope =  f'{dx // d}/{dy // d}'

                slope_counts[slope] += 1

            i_max = max(slope_counts.values(), default=0) + n_source_points
            max_n = max(max_n, i_max)

        return max_n



# @lc code=end

