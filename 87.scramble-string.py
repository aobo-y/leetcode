#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
from collections import Counter
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        cache = {}

        def check(s1, s2):
            key = (s1, s2)
            if key not in cache:
                if s1 == s2:
                    cache[key] = True
                elif Counter(s1) == Counter(s2):
                    res = False
                    for i in range(1, len(s1)):
                        l1, r1 = s1[:i], s1[i:]

                        l2, r2 = s2[:i], s2[i:]
                        if check(l1, l2) and check(r1, r2):
                            res = True
                            break
                        l2, r2 = s2[:-i], s2[-i:]
                        if check(l1, r2) and check(r1, l2):
                            res = True
                            break
                    cache[key] = res
                else:
                    cache[key] = False

            return cache[key]

        return check(s1, s2)


# @lc code=end

