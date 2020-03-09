#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w for w in s.split(' ') if w][::-1])

# @lc code=end

