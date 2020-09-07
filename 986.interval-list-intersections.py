#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        r = []
        while i < len(A) and j < len(B):
            t1, t2 = A[i], B[j]

            s, e = max(t1[0], t2[0]), min(t1[1], t2[1])
            if s <= e:
                r.append([s, e])

            if t1[1] <= t2[1]:
                i += 1
            if t1[1] >= t2[1]:
                j += 1

        return r

# @lc code=end

