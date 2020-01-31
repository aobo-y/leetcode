#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        start_bound = None

        max_len = 0

        i = 0

        for i, c in enumerate(s):
            if c == '(':
                if start_bound is None:
                    start_bound = i

                stack.append(i)
            elif stack:
                stack.pop()

                start = stack[-1] + 1 if stack else start_bound

                length = i - start + 1

                if length > max_len:
                    max_len = length
            else:
                start_bound = None


        return max_len

# @lc code=end

