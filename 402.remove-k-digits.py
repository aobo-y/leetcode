#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for l in num:
            d = int(l)

            while stack and k > 0 and d < stack[-1]:
                stack.pop()
                k -= 1

            if stack or d != 0:
                stack.append(d)

        while stack and k > 0:
            stack.pop()
            k -= 1

        return ''.join([str(i) for i in stack]) if stack else '0'
# @lc code=end

