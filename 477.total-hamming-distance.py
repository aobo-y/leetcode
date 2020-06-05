#
# @lc app=leetcode id=477 lang=python3
#
# [477] Total Hamming Distance
#

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # return sum([
        #     bin(nums[i] ^ nums[j]).count('1')
        #     for i in range(len(nums) - 1)
        #     for j in range(i + 1, len(nums))
        # ])
        if not nums:
            return 0

        n_ones = [0] * len(bin(max(nums))[2:])
        for num in nums:
            for i, d in enumerate(bin(num)[:1:-1]): # 0bxxx binary formay
                if d == '1':
                    n_ones[i] += 1

        return sum(c * (len(nums) - c) for c in n_ones)

# @lc code=end

