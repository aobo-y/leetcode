#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(target_, from_idx=0, idxes=[]):
            for i in range(from_idx, len(candidates)):
                num = candidates[i]

                if num == target_:
                    results.append(idxes + [num])
                elif num < target_:
                    dfs(target_ - num, i, idxes + [num])

        dfs(target)

        return results




# @lc code=end

