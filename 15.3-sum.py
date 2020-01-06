#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        sorted_nums = sorted(nums)
        length = len(sorted_nums)

        for i, num in enumerate(sorted_nums):
            if i > 0 and num == sorted_nums[i - 1]:
                continue

            target = -num
            l, r = i + 1, length - 1

            # need < instead of != coz l can go out of range
            while l < r:
                nums_sum = sorted_nums[l] + sorted_nums[r]

                if nums_sum > target:
                    r -= 1
                elif nums_sum < target:
                    l += 1
                else:
                    results.append([num, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1
        return results

# @lc code=end

