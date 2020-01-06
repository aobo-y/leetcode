#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        length = len(nums)
        results = []

        for i in range(0, length - 3):
            num1 = sorted_nums[i]

            if i > 0 and num1 == sorted_nums[i - 1]:
                continue

            for j in range(i + 1, length - 2):
                num2 = sorted_nums[j]

                if j > i + 1 and num2 == sorted_nums[j - 1]:
                    continue

                l, r = j + 1, length - 1

                while l < r:
                    num_l, num_r = sorted_nums[l], sorted_nums[r]
                    num_sum = num1 + num2 + num_l + num_r

                    if num_sum < target:
                        l += 1
                    elif num_sum > target:
                        r -= 1
                    else:
                        results.append([num1, num2, num_l, num_r])

                        l += 1
                        r -= 1

                        while l < r and sorted_nums[l] == num_l:
                            l += 1
                        while l < r and sorted_nums[r] == num_r:
                            r -= 1

        return results


# @lc code=end

