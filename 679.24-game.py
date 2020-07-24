#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#

# @lc code=start
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        for i, num1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                rest = [n for k, n in enumerate(nums) if k != i and k != j]

                cans = [
                    num1 + num2,
                    num1 - num2,
                    num2 - num1,
                    num1 * num2,
                ]

                if num1:
                    cans.append(num2 / num1)
                if num2:
                    cans.append(num1 / num2)

                for v in cans:
                    if not rest:
                        if round(v, 1) == 24.0:
                            return True
                    else:
                        if self.judgePoint24([v] + rest):
                            return True

        return False

# @lc code=end

