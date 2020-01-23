#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

# @lc code=start
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        # aX - b = Y where a = 2^i and b = L * 2^k1 + 2 ^ k2 + ... + 2^kn + c (k1...kn <= i, c = 0|1)
        # while j > 0: b % 2^j if j <= i

        # never need continuous decrement except beginning, coz if need decrease more than 2, should decrease beefore previous multiplications

        def fulfil_gap():
            a = 1
            i = 0
            steps = 0

            while a * X < Y:
                a *= 2
                i += 1
                steps += 1

            b = a * X - Y
            div = 2 ** i

            # greedily fulfill the gap
            while b != 0:
                if b >= div:
                    steps += b // div
                    b %= div
                div //= 2

            return steps

        def backward():
            v = Y
            steps = 0

            while v > X:
                steps += 1
                if v % 2 == 0:
                    v //= 2
                else:
                    v += 1
            steps += X - v

            return steps

        return backward()


# @lc code=end

