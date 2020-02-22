#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        prod = 1
        for i in range(1, n + 1):
            prod *= i

        nums = [i for i in range(1, n + 1)]
        res = ''
        div = prod
        k -= 1 # make idx start from 0

        for i in range(n, 0, -1):
            div = int(div / i)
            idx = k // div
            v = nums[idx]
            res += str(v)
            nums.remove(v)

            k %= div

        return res



# @lc code=end

