#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1_cp = nums1[:m]

        # i, j = 0, 0

        # for k in range(m + n):
        #     val1 = nums1_cp[i] if i < m else float('inf')
        #     val2 = nums2[j] if j < n else float('inf')

        #     if val1 < val2:
        #         nums1[k] = val1
        #         i += 1
        #     else:
        #         nums1[k] = val2
        #         j += 1

        i, j = m - 1, n - 1

        for k in range(m + n - 1, -1, -1):
            if i < 0 or j < 0:
                break

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

        if j >= 0:
            nums1[:j+1] = nums2[:j+1]





# @lc code=end

