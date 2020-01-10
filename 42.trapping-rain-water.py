#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left_bound_idx = 0

        amount = 0
        low_bound_height = 0

        for i, h in enumerate(height):

            if i > 0 and h > height[i - 1]:
                for j in range(i - 1, left_bound_idx - 1, -1):
                    if height[j] > low_bound_height:
                        min_height = min([height[j], h])
                        amount += (min_height - low_bound_height) * (i - j - 1)
                        low_bound_height = min_height

                    if height[j] >= h:
                        break

                if height[i] >= height[left_bound_idx]:
                    left_bound_idx = i
                    low_bound_height = h

            elif i > 0 and h < height[i - 1]:
                low_bound_height = h


        return amount


# @lc code=end

