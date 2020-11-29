#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = Counter(s)

        res = []
        visited = set()
        for c in s:
            counts[c] -= 1

            if c in visited:
                continue

            while res and res[-1] > c and counts[res[-1]] > 0:
                cc = res.pop()
                visited.remove(cc)

            res.append(c)
            visited.add(c)

        return ''.join(res)


# @lc code=end

