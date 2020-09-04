#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        isvalid = lambda i, j: s[i:j+1] == s[i:j+1][::-1]

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return isvalid(i, j - 1) or isvalid(i + 1, j)

        return True

# @lc code=end

