#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        l = len(nums)
        indices = [0] * l
        h = [(n[0], i) for i, n in enumerate(nums)]
        max_v = max(h)[0]
        heapq.heapify(h)

        r, r_v = None, float('inf')

        while True:
            min_v, min_idx = heapq.heappop(h)
            if max_v - min_v < r_v:
                r_v = max_v - min_v
                r = [min_v, max_v]

            indices[min_idx] += 1
            if indices[min_idx] == len(nums[min_idx]):
                break

            n_v = nums[min_idx][indices[min_idx]]
            heapq.heappush(h, (n_v, min_idx))
            max_v = max(max_v, n_v)

        return r


# @lc code=end

