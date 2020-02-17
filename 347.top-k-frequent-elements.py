#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        def use_heap():
            heap = [None] + [(v, c) for v, c in counts.items()]

            def heapify(j):
                if j > (len(heap) - 1) // 2:
                    return

                l, r = 2 * j, 2 * j + 1
                lv = heap[l][1]
                rv = heap[r][1] if r < len(heap) else float('-inf')

                v = heap[j][1]
                if v < lv and lv >= rv:
                    heap[j], heap[l] = heap[l], heap[j]
                    heapify(l)
                elif v < rv and rv >= lv:
                    heap[j], heap[r] = heap[r], heap[j]
                    heapify(r)

            n = len(heap) - 1
            for i in range(n // 2, 0, -1):
                heapify(i)

            res = []
            for _ in range(k):
                res.append(heap[1][0])
                tmp = heap.pop()
                if len(heap) > 1:
                    heap[1] = tmp
                    heapify(1)

            return res

        def use_bucket():
            buckets = [[] for _ in range(len(nums))]
            for v, c in counts.items():
                buckets[c - 1].append(v)

            res = []
            for vs in buckets[::-1]:
                res += vs
                if len(res) >= k:
                    break
            return res

        return use_bucket()


# @lc code=end

