#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        title = ''

        while n:
            n -= 1
            title += chr(65 + n % 26)
            n //= 26

        return title[::-1]

# @lc code=end

