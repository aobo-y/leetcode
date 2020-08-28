#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_num_1, min_num_2 = float('inf'), float('inf')
        for n in nums:
            if n > min_num_2:
                return True

            elif n > min_num_1:
                min_num_2 = n

            else:
                min_num_1 = n
        return False


# @lc code=end

