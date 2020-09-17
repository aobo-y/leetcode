#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        token = ''
        for c in s + ' ':
            if c.isdigit():
                token += c
                continue

            if token:
                stack.append(int(token))
                token = ''

            if len(stack) > 1 and stack[-2] in ['*', '/']:
                opr2 = stack.pop()
                opt = stack.pop()
                opr1 = stack.pop()
                r = opr1 * opr2 if opt == '*' else opr1 // opr2
                stack.append(r)

            if c != ' ':
                stack.append(c)

        r = stack[0]
        for i in range(1, len(stack), 2):
            opt = stack[i]
            opr = stack[i+1]

            r = r + opr if opt == '+' else r - opr

        return r


# @lc code=end

