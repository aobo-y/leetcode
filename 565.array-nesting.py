#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#

# @lc code=start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()

        max_len = 0

        for num in nums:
            if num in visited:
                continue

            visited.add(num)
            length = 1

            while nums[num] not in visited:
                num = nums[num]
                visited.add(num)

                length += 1

            if length > max_len:
                max_len = length

        return max_len



# @lc code=end

