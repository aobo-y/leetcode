#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m = len(M)
        n = len(M[0]) if M else 0

        R = [
            [0] * n
            for _ in range(m)
        ]

        for i in range(m):
            for j in range(n):
                cells = []
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni = i + di
                        nj = j + dj
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            continue

                        cells.append(M[ni][nj])

                R[i][j] = sum(cells) // len(cells)

        return R


# @lc code=end

