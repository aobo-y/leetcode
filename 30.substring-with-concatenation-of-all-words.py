#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []

        res = []

        wl = len(words[0])

        for offset in range(wl):
            wc = Counter(words)
            matched = 0

            for i in range(offset, len(s), wl):
                w = s[i:i+wl]
                while wc[w] == 0 and matched > 0:
                    rw = s[i-matched*wl:i-matched*wl+wl]
                    wc[rw] += 1
                    matched -= 1

                if wc[w] > 0:
                    wc[w] -= 1
                    matched += 1

                if matched == len(words):
                    res.append(i - matched * wl + wl)

        return res

# @lc code=end

