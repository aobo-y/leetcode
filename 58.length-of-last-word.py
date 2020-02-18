#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        for c in s[::-1]:
            if c != ' ':
                l += 1
            elif l != 0:
                break

        return l

# @lc code=end

