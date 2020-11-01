#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        max_idx = {}
        for i, c in enumerate(S):
            max_idx[c] = i

        r = []
        left, right = 0, 0
        for i, c in enumerate(S):
            right = max(right, max_idx[c])
            if i == right:
                r.append(right - left + 1)
                left = i + 1

        return r

# @lc code=end

