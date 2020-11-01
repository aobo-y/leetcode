#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s = {}
        c = 0

        for n in nums:
            if n in s:
                if not k and not s[n]:
                    c += 1
                    s[n] = True
                continue

            if n + k in s:
                c += 1
            if n - k in s:
                c += 1
            s[n] = False

        return c

# @lc code=end

