#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    from functools import lru_cache
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws = set(wordDict)

        l = len(s)

        @lru_cache(None)
        def breakable(i):
            if s[i:] in ws:
                return True

            for k in range(i + 1, l):
                if s[i:k] in ws and breakable(k):
                    return True

            return False

        return breakable(0)


# @lc code=end

