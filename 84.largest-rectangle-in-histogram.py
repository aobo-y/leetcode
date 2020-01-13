#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for i, height in enumerate(heights):
            min_height = height

            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                area = min_height * (j - i + 1)
                if area > max_area:
                    max_area = area

        return max_area

# @lc code=end

