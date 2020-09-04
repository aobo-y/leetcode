#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # nlogn
        def m1():
            return [p for p in sorted(points, key=lambda t: t[0] ** 2 + t[1] ** 2)[:K]]

        # nlogk
        def m2():
            h = []
            for p in points:
                heapq.heappush(h, (- p[0] ** 2 - p[1] ** 2, p))
                if len(h) > K:
                    heapq.heappop(h)

            return [p for _, p in h]

        return m2()

# @lc code=end

