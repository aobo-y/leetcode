#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)

        def method_dp():
            dp = [[0] * l for _ in range(l)]
            for i in range(l):
                dp[i][i] = 1

            for d in range(1, l):
                for i in range(0, l - d):
                    j = i + d
                    if s[i] != s[j]:
                        continue

                    dp[i][j] = dp[i+1][j-1] if i + 1 <= j - 1 else 1

            return sum(v for row in dp for v in row)


        def method_expand():
            c = 0
            for i in range(l):
                k = 0
                while i - k >= 0 and i + k < l and s[i-k] == s[i+k]:
                    c += 1
                    k += 1

                k = 0
                while i - k >= 0 and i + k + 1 < l and s[i-k] == s[i+k+1]:
                    c += 1
                    k += 1

            return c

        return method_expand()

# @lc code=end

