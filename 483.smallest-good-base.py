#
# @lc app=leetcode id=483 lang=python3
#
# [483] Smallest Good Base
#

# @lc code=start
import math
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_l = int(math.ceil(math.log(n, 2)))

        for l in range(max_l, 2, -1):
            # if let l becomes 1, below will cause precision issue
            max_k = int(n ** ((l - 1) ** -1))

            min_k = 2

            while min_k <= max_k:
                m = (min_k + max_k) // 2

                v = (m ** l - 1) // (m - 1)
                if v < n:
                    min_k = m + 1
                elif v > n:
                    max_k = m - 1
                else:
                    return str(m)

        return str(n - 1)

# @lc code=end

