#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph.lower()
        b = set(banned)

        counts = Counter()
        left = 0
        for i, c in enumerate(p + ' '):
            if ord('a') <= ord(c) <= ord('z'):
                continue

            if i > left:
                w = p[left:i]
                if w not in b:
                    counts[w] += 1

            left = i + 1

        m = max(counts.values())

        for w, v in counts.items():
            if v == m:
                return w


# @lc code=end

