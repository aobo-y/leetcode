#
# @lc app=leetcode id=1131 lang=python3
#
# [1131] Maximum of Absolute Value Expression
#

# @lc code=start
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        min1, max1 = min(arr1), max(arr1)
        min2, max2 = min(arr2), max(arr2)
        mini, maxi = 0, len(arr1) - 1

        pairs = [
            [(min1, min2, mini), (max1, max2, maxi)],
            [(max1, min2, mini), (min1, max2, maxi)],
            [(min1, max2, mini), (max1, min2, maxi)],
            [(max1, max2, mini), (min1, min2, maxi)],
        ]

        # mins = [
        #     [float('inf'), float('inf')]
        #     for _ in pairs
        # ]
        distances = [
            [float('inf'), float('-inf')]
            for _ in pairs
        ]

        for i, (v1, v2) in enumerate(zip(arr1, arr2)):
            for j, pair in enumerate(pairs):
                # for k, point in enumerate(pair):
                #     d = sum(abs(x1 - x2) for x1, x2 in zip(point, (v1, v2, i)))
                #     mins[j][k] = min(d, mins[j][k])
                d = sum(abs(x1 - x2) for x1, x2 in zip(pair[0], (v1, v2, i)))
                distances[j][0] = min(d, distances[j][0])
                distances[j][1] = max(d, distances[j][1])


        # dia_d = max1 - min1 + max2 - min2 + maxi - mini

        # max_d = max(dia_d - d1 - d2 for d1, d2 in mins)
        max_d = max(max_d - min_d for min_d, max_d in distances)

        return max_d



# @lc code=end

