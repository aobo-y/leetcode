#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            sum_ = numbers[i] + numbers[j]
            if sum_ > target:
                j -= 1
            elif sum_ < target:
                i += 1
            else:
                return [i + 1, j + 1] # index start in 1 in this Q

        return []
# @lc code=end

