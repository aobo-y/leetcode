#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        def find_set(subset, start_idx):
            if start_idx < len(nums):
                for i in range(start_idx, len(nums)):
                    num = nums[i]
                    new_set = subset + [num]
                    results.append(new_set)
                    find_set(new_set, i + 1)

        find_set([], 0)

        return results

# @lc code=end

