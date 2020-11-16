#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        for i in range(len(s), 0, -1):
            if s[:i] == s[:i][::-1]:
                break

        return s[i:][::-1] + s

# @lc code=end

