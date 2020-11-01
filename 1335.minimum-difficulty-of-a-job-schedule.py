#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#

# @lc code=start
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        cache = {}

        def find(i, dd):
            if i < len(jobDifficulty) and not dd:
                return -1
            if i == len(jobDifficulty) and dd:
                return -1
            if i == len(jobDifficulty) and not dd:
                return 0

            k = (i, dd)
            if k in cache:
                return cache[k]

            m = 0
            min_r = -1

            for j in range(i, len(jobDifficulty)):
                m = max(m, jobDifficulty[j])

                r = find(j + 1, dd - 1)
                if r != -1:
                    if min_r == -1:
                        min_r = m + r
                    else:
                        min_r = min(min_r, m + r)

            cache[k] = min_r
            return min_r

        return find(0, d)
# @lc code=end

