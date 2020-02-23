#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l < r:
            i = (l + r + 1) // 2 # choose right element when there are two becoz we can not shrink l if left is smaller than x
            p = i * i
            if p > x:
                r = i - 1
            elif p < x:
                l = i
            else:
                return i
        return l

# @lc code=end

