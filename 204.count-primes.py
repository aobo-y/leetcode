#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        primes = [1] * n
        primes[0], primes[1] = 0, 0

        for i in range(2, int(n ** 0.5) + 1):
            if primes:
                for j in range(i ** 2, n, i):
                    primes[j] = 0

        return sum(primes)



# @lc code=end

