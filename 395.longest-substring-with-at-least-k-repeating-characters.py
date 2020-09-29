#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
from collections import Counter, defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        rm_c = {c for c, v in Counter(s).items() if v < k}

        rm_pos = [i for i, c in enumerate(s) if c in rm_c]
        if not rm_pos:
            return len(s)

        rm_pos.append(len(s))
        r, i = 0, 0
        for p in rm_pos:
            if i < p:
                r = max(r, self.longestSubstring(s[i:p], k))
            i = p + 1

        return r


# @lc code=end

