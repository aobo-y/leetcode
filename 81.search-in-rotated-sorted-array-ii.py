#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums)

        def find(start, end):
            if start > end:
                return False

            idx = (start + end) // 2
            v = nums[idx]

            if v == target:
                return True

            while nums[start] == v and start < idx:
                start += 1
            while nums[end] == v and end > idx:
                end -= 1

            if nums[start] <= v:
                if target >= nums[start] and target < v:
                    return find(start, idx - 1)
                else:
                    return find(idx + 1, end)

            else:
                if target > v and target <= nums[end]:
                    return find(idx + 1, end)
                else:
                    return find(start, idx - 1)

        return find(0, len(nums) - 1)


# @lc code=end

