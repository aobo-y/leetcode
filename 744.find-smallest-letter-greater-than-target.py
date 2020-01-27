#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s, e = 0, len(letters) - 1

        while s < e:
            idx = (s + e) // 2

            v = letters[idx]

            if target >= v:
                s = idx + 1
            elif target < v:
                e = idx

        return letters[s] if letters[s] > target else letters[0]

# @lc code=end

