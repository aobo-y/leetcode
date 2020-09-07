#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if not carry:
                break

            d = int(digits[i]) + carry
            digits[i], carry = d % 10, d // 10

        if carry:
            digits = [carry] + digits

        return digits

# @lc code=end

