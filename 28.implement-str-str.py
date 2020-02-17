#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        nl = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if all(haystack[i+k] == needle[k] for k in range(nl)):
                return i

        return -1
# @lc code=end

