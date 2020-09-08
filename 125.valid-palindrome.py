#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def iter_char():
            s = s.lower()
            l, r = 0, len(s) - 1
            valid = lambda i: (i >= ord('a') and i <= ord('z')) or (i >= ord('0') and i <= ord('9'))

            while l <= r:
                lc, rc = s[l], s[r]
                if not valid(ord(lc)):
                    l += 1
                elif not valid(ord(rc)):
                    r -= 1
                elif lc == rc:
                    l += 1
                    r -= 1
                else:
                    return False

            return True

        def reverse_str():
            ns = ''.join(c for c in s.lower() if (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9'))

            return ns == ns[::-1]

        return reverse_str()

# @lc code=end

