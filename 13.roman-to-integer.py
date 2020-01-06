#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        i = 0

        while i < len(s):
            char = s[i]
            next_char = s[i + 1] if i + 1 < len(s) else ''

            if char == 'I':
                if next_char == 'V':
                    result += 4
                    i += 1
                elif next_char == 'X':
                    result += 9
                    i += 1
                else:
                    result += 1

            elif char == 'V':
                result += 5

            elif char == 'X':
                if next_char == 'L':
                    result += 40
                    i += 1
                elif next_char == 'C':
                    result += 90
                    i += 1
                else:
                    result += 10

            elif char == 'L':
                result += 50

            elif char == 'C':
                if next_char == 'D':
                    result += 400
                    i += 1
                elif next_char == 'M':
                    result += 900
                    i += 1
                else:
                    result += 100

            elif char == 'D':
                result += 500

            elif char == 'M':
                result += 1000

            i += 1

        return result

# @lc code=end

