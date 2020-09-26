#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def linear():
            p = None
            for i, a in enumerate(arr):
                p = i
                if a > x:
                    break

            l, r = p - 1, p
            while r - 1 - l < k:
                if l < 0:
                    r += 1
                elif r > len(arr) - 1:
                    l -= 1
                elif arr[r] - x < x - arr[l]:
                    r += 1
                else:
                    l -= 1

            return arr[l+1:r]

        def binary_search():
            i, j = 0, len(arr) - k

            while i < j:
                m = (i + j) // 2
                if arr[m+k] < x:
                    i = m + 1
                elif arr[m] > x:
                    j = m
                elif abs(x - arr[m]) > abs(arr[m+k] - x):
                    i = m + 1
                else:
                    j = m

            return arr[i:i+k]

        return binary_search()



# @lc code=end

