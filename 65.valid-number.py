#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        if s[0] == '+' or s[0] == '-':
            s = s[1:]

        tokens = s.split('e')
        if len(tokens) > 2:
            return False

        for i, token in enumerate(tokens):
            if not token:
                return False

            if token[0] == '+' or token[0] == '-':
                token = token[1:]
                if not token:
                    return False
                tokens[i] = token


        decimal = False
        for i, c in enumerate(tokens[0]):
            if c == '.':
                if (i == 0 and len(tokens[0]) == 1) or decimal:
                    return False
                decimal = True
            elif not c.isdigit():
                return False

        if len(tokens) == 2:
            for i, c in enumerate(tokens[1]):
                if not c.isdigit():
                    return False

        return True




# @lc code=end

