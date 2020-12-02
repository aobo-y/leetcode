#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []

        lh, rh = [], []
        pos = [None] * len(nums)  # num in left or right heap

        lc, rc = 0, 0
        for i, n in enumerate(nums):
            if i - k >= 0:
                rm_heap = pos[i-k]
                if rm_heap == 'l':
                    lc -= 1
                else:
                    rc -= 1

            if rh and rh[0][0] <= n:
                heapq.heappush(rh, (n, i))
                pos[i] = 'r'
                rc += 1
            else:
                heapq.heappush(lh, (-n, i))
                pos[i] = 'l'
                lc += 1

            while lh and (lc - rc > 1 or lh[0][1] <= i - k):
                ln, li = heapq.heappop(lh)
                if li > i - k:
                    heapq.heappush(rh, (-ln, li))
                    lc -= 1
                    rc += 1
                    pos[li] = 'r'

            while rh and (rc - lc > 1 or rh[0][1] <= i - k):
                rn, ri = heapq.heappop(rh)
                if ri > i - k:
                    heapq.heappush(lh, (-rn, ri))
                    lc += 1
                    rc -= 1
                    pos[ri] = 'l'

            if i >= k - 1:
                if lc > rc:
                    res.append(-lh[0][0])
                elif lc < rc:
                    res.append(rh[0][0])
                else:
                    res.append((-lh[0][0] + rh[0][0]) / 2)

        return res


# @lc code=end

