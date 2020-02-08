#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        i = 0

        while True:
            c_set = set(w[i] if i < len(w) else '' for w in strs)

            if len(c_set) > 1 or '' in c_set:
                break

            i += 1

        return strs[0][:i]

# @lc code=end

