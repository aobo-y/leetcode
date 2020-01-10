#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        i = 0

        left, right = None, None
        while True:
            if i < len(intervals):
                interval = intervals[i]
                if newInterval and interval[0] > newInterval[0]:
                    interval = newInterval
                    newInterval = None
                else:
                    i += 1
            elif newInterval:
                interval = newInterval
                newInterval = None
            else:
                break

            if left is None:
                left, right = interval
            elif right < interval[0]:
                result.append([left, right])
                left, right = interval
            else:
                right = max(right, interval[1])

        result.append([left, right])


        return result


# @lc code=end

