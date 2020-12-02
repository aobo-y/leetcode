#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        state = {(0, 0): 0}
        for s in strs:
            counts = Counter(s)
            for k, v in list(state.items()):
                nk = (k[0] + counts['0'], k[1] + counts['1'])
                if nk[0] > m or nk[1] > n:
                    continue

                if nk not in state or state[nk] < v + 1:
                    state[nk] = v + 1

        return max(state.values())


# @lc code=end

