#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        s = sum(A)

        base = sum(
            i * v for i, v in enumerate(A)
        )

        l = len(A)
        m = base
        for i in range(1, l):
            v = A[-i]
            base = base + s - l * v
            m = max(m, base)

        return m
# @lc code=end

