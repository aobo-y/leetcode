#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
from collections import Counter
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        d_counts = Counter(s)

        d = 9
        for i, c in enumerate(s):
            while not d_counts[str(d)]:
                d -= 1

            if c != str(d):
                j = s.rindex(str(d))
                num = [c for c in s]
                num[i], num[j] = num[j], num[i]
                num = int(''.join(num))
                break

            d_counts[str(d)] -= 1

        return num



# @lc code=end

