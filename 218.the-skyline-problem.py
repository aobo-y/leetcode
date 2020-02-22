#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def scan():
            cords = []
            for l, r, h in buildings:
                cords.append((l, h, r))
                cords.append((r, 0, None))

            # go up -> go down; heigh -> low
            cords = sorted(cords, key=lambda c: c[1], reverse=True)
            cords = sorted(cords, key=lambda c: c[0])

            res = []
            active_heights = []

            for x, h, r in cords:
                while active_heights and active_heights[0][1] <= x:
                    heapq.heappop(active_heights)

                if h > 0:
                    heapq.heappush(active_heights, (-h, r))

                ch = -active_heights[0][0] if active_heights else 0
                if not res or ch != res[-1][1]:
                    res.append([x, ch])

            return res

        # memory error for test case [[0,2147483647,2147483647]]
        def hitmap():
            max_r = max([b[1] for b in buildings], default=0)
            hm = [0] * (max_r + 1)

            for l, r, h in buildings:
                for i in range(l, r):
                    hm[i] = max(h, hm[i])

            res = []
            ch = 0
            for i, h in enumerate(hm):
                if ch != h:
                    ch = h
                    res.append([i, ch])

            return res

        return scan()




    # @lc code=end

