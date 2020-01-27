#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
import re

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return

        s = s.replace(' ', '')
        tokens = re.split('([+\-\(\)])', s)
        stack = []
        i = 0

        for token in tokens:
            if not token:
                continue

            if token == ')':
                token = stack.pop()
                stack.pop() # pop (

            if token == '(' or token == '+' or token == '-':
                stack.append(token)
            else:
                token = int(token)
                if stack and stack[-1] != '(':
                    opt = stack.pop()
                    opr1 = stack.pop()
                    token = token + opr1 if opt == '+' else opr1 - token

                stack.append(token)

        return stack.pop()


# @lc code=end

