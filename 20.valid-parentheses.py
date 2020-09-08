#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c not in match:
                stack.append(c)
            elif not stack or stack.pop() != match[c]:
                return False

        return not stack

# @lc code=end

