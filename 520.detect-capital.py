#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return all(ord('A') <= ord(c) <= ord('Z') for c in word) \
          or all(ord('a') <= ord(c) <= ord('z') for c in word) \
          or (
              ord('A') <= ord(word[0]) <= ord('Z') and all(ord('a') <= ord(c) <= ord('z') for c in word[1:])
          )

# @lc code=end

