#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        dias = []
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if i + j >= len(dias):
                    dias.append([])

                dias[i+j].append(v)

        return [
            v
            for i, dia in enumerate(dias)
            for v in dia[::(1 if i % 2 else -1)]
        ]

# @lc code=end

