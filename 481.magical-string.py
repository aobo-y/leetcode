#
# @lc app=leetcode id=481 lang=python3
#
# [481] Magical String
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        occ_ptr = 2
        char = 1

        while len(s) < n:
            occ = s[occ_ptr]
            for _ in range(occ):
                s.append(char)

            char = 1 if char == 2 else 2
            occ_ptr += 1

        return len([v for v in s[:n] if v == 1])

# @lc code=end

