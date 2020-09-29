#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        l, r = newInterval
        for s, e in intervals:
            if e < l:
                result.append([s, e])
            elif s > r:
                result.append([l, r])
                l, r = s, e
            else:
                l = min(l, s)
                r = max(r, e)

        result.append([l, r])
        return result


# @lc code=end

