#
# @lc app=leetcode id=514 lang=python3
#
# [514] Freedom Trail
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_pos = defaultdict(list)
        for i, c in enumerate(ring):
            char_pos[c].append(i)

        state = {0: 0}  # pos: steps
        l = len(ring)

        for c in key:
            state = {
                pos: min(
                    min(abs(pos - pp), l - abs(pos - pp)) + ps
                    for pp, ps in state.items()
                ) + 1
                for pos in char_pos[c]
            }

        return min(state.values())


# @lc code=end

