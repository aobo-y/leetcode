#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
class Solution:
    import random
    def __init__(self, w: List[int]):
        accum_counts = []
        a = 0
        for p in w:
            a += p
            accum_counts.append(a)

        self.accum_counts = accum_counts


    def pickIndex(self) -> int:
        v = random.randint(1, self.accum_counts[-1])

        l, r = 0, len(self.accum_counts) - 1
        while l < r:
            k = (l + r) // 2

            if v <= self.accum_counts[k]:
                r = k
            else:
                l = k + 1

        return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

