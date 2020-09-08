#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return all(i >= j for i, j in zip(A, A[1:])) or all(i <= j for i, j in zip(A, A[1:]))

# @lc code=end

