#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    cache = {}

    def numSquares(self, n: int) -> int:
        def recur():
            if not n:
                return 0

            if n in self.cache:
                return self.cache[n]

            u = int(n ** 0.5)
            l = u // 2

            m = float('inf')
            for i in range(l + 1, u + 1):
                k = i ** 2
                m = min(m, n // k + self.numSquares(n % k))

            self.cache[n] = m
            return m

        def dp():
            l = [float('inf')] * (n + 1)
            l[0] = 0

            for t in range(1, n + 1):
                for i in range(int(t ** 0.5) // 2, int(t ** 0.5) + 1):
                    l[t] = min(l[t], l[t - i ** 2] + 1)

            return l[n]

        return recur()

# @lc code=end

