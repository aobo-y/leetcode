#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_res = 0

        while l < r:
            lv, rv = height[l], height[r]
            size = (r - l) * min([lv, rv])

            if size > max_res:
                max_res = size

            if lv > rv:
                r -= 1
                while height[r] <= rv and l < r:
                    r -= 1
            elif lv < rv:
                l += 1
                while height[l] <= lv and l < r:
                    l += 1
            else:
                l_, r_ = l, r
                while l_ < r_:
                    l_ += 1
                    if height[l_] > lv:
                        l = l_
                        break

                    r_ -= 1
                    if height[r_] > rv:
                        r = r_
                        break

                if l_ >= r_:
                    break

        return max_res



# @lc code=end

