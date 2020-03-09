#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0

        for _ in range(32):
            r <<= 1
            r |= n & 1 # mask other bit except last one
            n >>= 1

        return r

# @lc code=end

