#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        s_dict = {}

        def find(i):
            if i == len(s):
                return [[]]

            ss = s[i:]
            if ss in s_dict:
                return s_dict[ss]

            res = []
            for j in range(i, len(s)):
                token = s[i:j+1]
                if token in word_set:
                    for l in find(j + 1):
                        res.append([token, *l])

            s_dict[ss] = res

            return res

        return [' '.join(l) for l in find(0)]


# @lc code=end

