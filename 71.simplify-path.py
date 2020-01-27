#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        stack = []

        for token in tokens:
            if not token or token == '.':
                continue

            if token == '..':
                if stack:
                    stack.pop()
                continue

            stack.append(token)

        return '/' + '/'.join(stack)

# @lc code=end

