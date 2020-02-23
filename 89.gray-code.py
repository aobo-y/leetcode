#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        if n == 0:
            return res

        for i in range(1, n + 1):
            leading = 1 << (i - 1) # 2 ** (i-1)
            flip = [j | leading for j in res[::-1]] # j + leading
            res += flip

        return res



# @lc code=end

