#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def find(start, n_nums, target, path):
            results = []

            if n_nums == 2:
                i, j = start, 9
                while i < j:
                    if i + j > target:
                        j -= 1
                    elif i + j < target:
                        i += 1
                    else:
                        results.append(path + [i, j])
                        i += 1
                        j -= 1
                return results

            else:
                for i in range(start, 10):
                    if i >= target:
                        break

                    results += find(i + 1, n_nums - 1, target - i, path + [i])

                return results

        if k == 1:
            if n >= 1 and n <= 9:
                return [[n]]
            else:
                return []

        return find(1, k, n, [])
# @lc code=end

