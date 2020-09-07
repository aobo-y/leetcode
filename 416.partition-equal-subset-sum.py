#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        states = set([0])
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2

        for num in nums:
            states = set([
                nv
                for v in states
                for nv in [v + num, v]
                if nv <= target
            ])

        return target in states


# @lc code=end

