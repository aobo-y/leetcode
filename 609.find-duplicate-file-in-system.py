#
# @lc app=leetcode id=609 lang=python3
#
# [609] Find Duplicate File in System
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in paths:
            tokens = s.split(' ')
            p = tokens[0]

            for token in tokens[1:]:
                name, cnt = token.split('(')
                d[cnt[:-1]].append(p + '/' + name)

        return [g for _, g in d.items() if len(g) > 1]

# @lc code=end

