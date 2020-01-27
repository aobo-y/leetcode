#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        letters = []
        stack = []
        num = 0

        for l in s:
            if l.isdigit():
                num = num * 10 + int(l)
            elif l == '[':
                stack.append([letters, num])
                letters = []
                num = 0
            elif l == ']':
                preletters, num = stack.pop()
                letters = preletters + letters * num
                num = 0
            else:
                letters.append(l)

        return ''.join(letters)


# @lc code=end

