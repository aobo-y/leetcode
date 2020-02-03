#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for token in strs:
            key = ''.join(sorted(token))
            groups[key].append(token)

        return list(groups.values())

# @lc code=end

