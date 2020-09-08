#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        result = []

        sorted_intervals = sorted(intervals)

        left_val, right_val = sorted_intervals[0]

        for interval in sorted_intervals[1:]:
            if interval[0] > right_val:
                result.append([left_val, right_val])
                left_val, right_val = interval
            else:
                right_val = max(interval[1], right_val)

        result.append([left_val, right_val])

        return result
# @lc code=end

