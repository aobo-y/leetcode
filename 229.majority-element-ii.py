#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a, a_count = None, 0
        b, b_count = None, 0

        for num in nums:
            if num == a:
                a_count += 1
            elif num == b:
                b_count += 1
            elif a_count == 0:
                a, a_count = num, 1
            elif b_count == 0:
                b, b_count = num, 1
            else:
                a_count -= 1
                b_count -= 1

        results = {}
        if a_count != 0:
            results[a] = 0
        if b_count != 0:
            results[b] = 0

        for num in nums:
            if num in results:
                results[num] += 1

        return [n for n, c in results.items() if c > len(nums) // 3]

# @lc code=end

