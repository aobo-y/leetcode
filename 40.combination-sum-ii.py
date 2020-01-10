#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # avoid duplicates
        sorted_candidates = sorted(candidates)

        def dfs(target_, from_idx=0, nums=[]):
            for i in range(from_idx, len(sorted_candidates)):
                num = sorted_candidates[i]

                if i != from_idx and num == sorted_candidates[i - 1]:
                    continue

                if num == target_:
                    result.append(nums + [num])
                elif num < target_:
                    dfs(target_ - num, i + 1, nums + [num])

        dfs(target)

        return result

# @lc code=end

