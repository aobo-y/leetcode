#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or token.replace('-', '').isdigit():
                stack.append(int(token))
                continue

            opd2 = stack.pop()
            opd1 = stack.pop()

            if token == '+':
                res = opd1 + opd2
            elif token == '-':
                res = opd1 - opd2
            elif token == '*':
                res = opd1 * opd2
            elif token == '/':
                res = int(opd1 / opd2)

            stack.append(res)

        return stack.pop()

# @lc code=end

