#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        # critical to avoid duplicates nums like [1, 4, 1]
        nums = sorted(nums)

        def find_set(start_idx, prev_set):
            val_set = set()

            for i in range(start_idx, len(nums)):
                val = nums[i]
                if val in val_set:
                    continue

                val_set.add(val)
                new_set = prev_set + [val]
                results.append(new_set)

                find_set(i + 1, new_set)

        find_set(0, [])

        return results


# @lc code=end

