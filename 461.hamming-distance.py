#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return sum(int(i) for i in bin(x ^ y)[2:])
        return bin(x ^ y)[2:].count('1')

# @lc code=end

