#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr = 0
        l = 0
        chars = set()

        for i, c in enumerate(s):
            if c in chars:
                while s[ptr] != c:
                    chars.remove(s[ptr])
                    ptr += 1
                ptr += 1
            else:
                chars.add(c)

            l = max(l, i - ptr + 1)

        return l

# @lc code=end

