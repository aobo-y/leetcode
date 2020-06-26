#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mem = {}

        for i, c in enumerate(s):
            if c not in mem:
                mem[c] = i
            else:
                mem[c] = -1

        nr = [i for _, i in mem.items() if i >= 0]
        return min(nr) if nr else -1
# @lc code=end

