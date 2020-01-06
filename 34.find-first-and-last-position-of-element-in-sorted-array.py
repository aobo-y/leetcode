#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(left, right):
            if left > right:
                return [-1, -1]

            if nums[right] < target or nums[left] > target:
                return [-1, -1]

            # guard to skip [target ... target] case
            if nums[left] == target and nums[right] == target:
                return [left, right]

            i = (left + right) // 2

            if nums[i] > target:
                return find(left, i - 1)
            elif nums[i] < target:
                return find(i + 1, right)
            else:
                result = [i, i]

                if nums[left] == target:
                    result[0] = left
                else:
                    left_res = find(left, i - 1)
                    if left_res[0] != -1:
                        result[0] = left_res[0]

                if nums[right] == target:
                    result[1] = right
                else:
                    right_res = find(i + 1, right)
                    if right_res[1] != -1:
                        result[1] = right_res[1]


                return result

        return find(0, len(nums) - 1)




# @lc code=end

