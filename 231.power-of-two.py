#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # method 1
        return False if n <= 0 else not (n & (n - 1))

        # method 2
        i = 1
        while i < n:
            i *= 2

        return i == n

# @lc code=end

