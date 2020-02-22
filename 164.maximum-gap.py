#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_num, max_num = min(nums), max(nums)
        if max_num == min_num:
            return 0
        step = (max_num - min_num) / (len(nums) - 1)

        buckets = [[] for _ in nums]

        for num in nums:
            idx = int((num - min_num) // step)

            bucket = buckets[idx]
            if not bucket:
                bucket.append(num)
                bucket.append(num)
            elif num < bucket[0]:
                bucket[0] = num
            elif num > bucket[1]:
                bucket[1] = num

        max_gap = 0
        pre_bucket = buckets[0]
        for i in range(1, len(buckets)):
            bucket = buckets[i]
            if bucket:
                gap = bucket[0] - pre_bucket[1]
                if gap > max_gap:
                    max_gap = gap

                pre_bucket = bucket

        return max_gap


# @lc code=end

