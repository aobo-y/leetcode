#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        r = []
        b = 0
        for c in s:
            if c == '(':
                b += 1
            elif c == ')':
                if not b:
                    continue
                b -= 1

            r.append(c)

        s = r[::-1]
        r = []
        b = 0
        for c in s:
            if c == ')':
                b += 1
            elif c == '(':
                if not b:
                    continue
                b -= 1

            r.append(c)

        return ''.join(r[::-1])

# @lc code=end

