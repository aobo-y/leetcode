#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        pos_reached = 0
        start_pos = 0
        max_reach = 0
        steps_taken = 0

        while pos_reached < len(nums) - 1:
            for origin in range(start_pos, pos_reached + 1):
                max_jump = nums[origin]
                max_reach = max([max_reach, origin + max_jump])

            steps_taken += 1
            pos_reached, start_pos = max_reach, pos_reached + 1

        return steps_taken



# @lc code=end

