#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fst, scd, trd = float('-inf'), float('-inf'), float('-inf')

        for num in nums:
            if num > fst:
                fst, scd, trd = num, fst, scd
            elif num == fst:
                continue
            elif num > scd:
                scd, trd = num, scd
            elif num == scd:
                continue
            elif num > trd:
                trd = num
            else:
                continue

        if trd > float('-inf'):
            return trd
        else:
            return fst

# @lc code=end

