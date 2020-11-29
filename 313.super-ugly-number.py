#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        def method_nk():
            h = [(1, 0)]  # value, max factor idx

            for _ in range(n - 1):
                v, max_idx = heapq.heappop(h)
                for i in range(max_idx, len(primes)):
                    heapq.heappush(h, (v * primes[i], i))

            return heapq.heappop(h)[0]

        def method_nlgk():
            ugly = []
            prime_ptr = [0] * len(primes)
            h = [(1, p, 0) for p in primes]  # val, prime, ugly idx

            for _ in range(n):
                u = h[0][0]
                ugly.append(u)

                while h[0][0] == u:
                    _, p, idx = heapq.heappop(h)
                    heapq.heappush(h, (ugly[idx] * p, p, idx + 1))

            return ugly[-1]

        return method_nlgk()


# @lc code=end

