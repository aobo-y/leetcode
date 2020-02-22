#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]

        res = [
            com + [i]
            for i in range(k, n + 1)
            for com in self.combine(i - 1, k - 1)
        ]

        return res


    def combine_bk(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []

        reverse = False
        if k > n // 2:
            reverse, k = True, n - k

        layer = [[]]

        for j in range(0, k):
            new_layer = []
            for com in layer:
                s = com[-1] if len(com) > 0 else 0
                for i in range(s + 1, n + 1 - k + j + 1):
                    new_layer.append(com + [i])
            layer = new_layer

        if reverse:
            nums = set([i for i in range(1, n + 1)])
            layer = [
                list(nums - set(com))
                for com in layer
            ]

        return layer

# @lc code=end

