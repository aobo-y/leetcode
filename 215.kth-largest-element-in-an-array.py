#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [None] + nums

        def balance_heap(i):
            while True:
                val = heap[i]
                l, r = 2 * i, 2 * i + 1
                lv = heap[l] if l < len(heap) else float('-inf')
                rv = heap[r] if r < len(heap) else float('-inf')

                if lv <= rv and rv > val:
                    heap[i], heap[r] = heap[r], heap[i]
                    i = r
                elif lv > rv and lv > val:
                    heap[i], heap[l] = heap[l], heap[i]
                    i = l
                else:
                    break


        for i in range(len(nums) // 2, 0, -1):
            balance_heap(i)

        for j in range(k - 1):
            heap[1] = heap.pop()
            balance_heap(1)

        return heap[1]


# @lc code=end

