#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        i = 0
        while i < len(s) - i - 1:
            s[i], s[-i-1] = s[-i-1], s[i]
            i += 1

        return s

# @lc code=end

