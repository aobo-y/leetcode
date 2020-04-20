#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def compare():
            by_k = 2 * t + 1 >= k

            cache = {}
            for i, num in enumerate(nums):
                if by_k:
                    for num2 in nums[i+1:i+k+1]:
                        if abs(num - num2) <= t:
                            return True

                else: # by_t
                    for num2 in range(num - t, num + t + 1):
                        if num2 in cache and i - cache[num2] <= k:
                            return True

                        cache[num] = i


            return False

        def bucket():
            buckets = {}

            for i, num in enumerate(nums):
                idx = num // t if t else num
                for b_idx in range(idx - 1, idx + 2):
                    if b_idx in buckets:
                        num2, j = buckets[b_idx]
                        if abs(num - num2) <= t and abs(i - j) <= k:
                            return True

                buckets[idx] = (num, i)

            return False

        return bucket()



# @lc code=end

