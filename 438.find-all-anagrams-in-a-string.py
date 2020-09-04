#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def method_1():
            counts = Counter(p)
            r = []

            i, j = 0, len(p) - 1
            state = Counter(s[i:j])

            while j < len(s):
                state[s[j]] += 1

                if state == counts:
                    r.append(i)

                state[s[i]] -= 1
                if not state[s[i]]:
                    del state[s[i]]

                i += 1
                j += 1

            return r

        def method_2():
            counts = Counter(p)
            left = len(p)
            r = []

            i = 0
            for j, c in enumerate(s):
                if c in counts:
                    counts[c] -= 1
                    if counts[c] >= 0:
                        left -= 1

                if not left:
                    r.append(i)

                if j - i + 1 == len(p):
                    if s[i] in counts:
                        counts[s[i]] += 1
                        if counts[s[i]] > 0:
                            left += 1

                    i += 1

            return r

        return method_2()

# @lc code=end

