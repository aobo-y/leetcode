#
# @lc app=leetcode id=517 lang=python3
#
# [517] Super Washing Machines
#

# @lc code=start
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        s = sum(machines)
        if s % len(machines) != 0:
            return -1

        avg = s // len(machines)

        offsets = [v - avg for v in machines]

        diff = 0
        max_diff = 0
        for offset in offsets:
            diff += offset
            max_diff = max(max_diff, abs(diff))

        return max(max_diff, max(offsets))

# @lc code=end

