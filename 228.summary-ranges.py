#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        results = []

        start, end = None, None
        for i, num in enumerate(nums):
            if i == 0:
                start, end = num, num
            elif num == end + 1:
                end = num
            else:
                if start == end:
                    results.append(str(start))
                else:
                    results.append(f'{start}->{end}')

                start, end = num, num

            if i == len(nums) - 1:
                if start == end:
                    results.append(str(start))
                else:
                    results.append(f'{start}->{end}')

        return results




# @lc code=end

