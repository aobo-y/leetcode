#
# @lc app=leetcode id=564 lang=python3
#
# [564] Find the Closest Palindrome
#

# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        p = (l + 1) // 2
        left = n[:p]

        min_gap, min_val, res = float('inf'), None, None

        for adj in (0, 1, -1):
            left_ = str(int(left) + adj)
            rl = l - p

            if len(left_) > rl + 1:
                left_ = '1' + '0' * (len(left_) - 2)
                rl += 1
            elif len(left_) < rl:
                left_ = '9' * (len(left_) + 1)
                rl -= 1
            elif left_ == '0' and rl != 0:
                left_ = '9'
                rl -= 1

            s = left_ + left_[:rl][::-1]
            val = int(s)
            gap = abs(val - int(n))

            if gap < min_gap and gap != 0:
                res, min_val, min_gap = s, val, gap
            elif gap == min_gap and val < min_val:
                res, min_val = s, val

        return res

# @lc code=end

