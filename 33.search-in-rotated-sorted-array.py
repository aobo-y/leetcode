#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_idx(left, right):
            if right < left:
                return -1

            i = (left + right) // 2

            iv = nums[i]

            if iv == target:
                return i

            lv, rv = nums[left], nums[right]

            # error input case
            if rv < target < lv:
                return -1

            if lv < rv:
                if target < iv:
                    return find_idx(left, i - 1)
                else:
                    return find_idx(i + 1, right)
            elif iv < rv:
                if iv < target <= rv:
                    return find_idx(i + 1, right)
                else:
                    return find_idx(left, i - 1)
            else:
                if lv <= target < iv:
                    return find_idx(left, i - 1)
                else:
                    return find_idx(i + 1, right)

        return find_idx(0, len(nums) - 1)


# @lc code=end

