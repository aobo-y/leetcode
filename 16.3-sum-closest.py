#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        length = len(sorted_nums)
        closest = None

        for i, num in enumerate(sorted_nums[:-2]):
            l, r = i + 1, length - 1

            while l < r:
                nums_sum = sorted_nums[l] + sorted_nums[r] + num

                if closest is None or abs(nums_sum - target) < abs(closest - target):
                    closest = nums_sum

                if nums_sum < target:
                    l += 1
                elif nums_sum > target:
                    r -= 1
                else:
                    return nums_sum

        return closest



# @lc code=end

