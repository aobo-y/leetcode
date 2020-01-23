#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1

        start, end = 1, n
        v = None

        while True:
            v = (start + end) // 2

            large_count, small_count, count = 0, 0, 0

            for num in nums:
                if num > v:
                    large_count += 1
                elif num < v:
                    small_count += 1
                else:
                    count += 1

            if count > 1:
                break

            if small_count > v - 1:
                end = v - 1
            elif large_count > n - v:
                start = v + 1
            else:
                return None

        return v



# @lc code=end

