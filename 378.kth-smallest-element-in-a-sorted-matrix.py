#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(v, i, 0) for i, v in enumerate(matrix[0])]  # val, col, row
        heapq.heapify(heap)

        while k > 1:
            v, c, r = heapq.heappop(heap)
            if r < n - 1:
                heapq.heappush(heap, (matrix[r+1][c], c, r + 1))

            k -= 1

        return heapq.heappop(heap)[0]

# @lc code=end

