#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_dict = {w: True for w in wordDict}
        def breakable(i, j):
            ss = s[i:j]
            if ss not in s_dict:
                s_dict[ss] = False
                for k in range(i + 1, j):
                    if breakable(i, k) and breakable(k, j):
                        s_dict[ss] = True
                        break

            return s_dict[ss]

        return breakable(0, len(s))




# @lc code=end

