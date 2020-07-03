#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[None] * len(s) for _ in range(len(s))]

        for l in range(len(s)):
            for i in range(len(s) - l):
                j = i + l

                if i == j:
                    dp[i][j] = 1
                    continue

                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], 2 + (dp[i+1][j-1] if i + 1 <= j - 1 else 0))


        return dp[0][-1]
# @lc code=end

