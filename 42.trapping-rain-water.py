#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        blocks = 0
        amount = 0
        for i, h in enumerate(height):
            while stack and h > stack[-1][0]:
                b, j = stack.pop()
                if not stack:
                    amount += b * (i - j - 1)
                else:
                    blocks += b

            stack.append((h, i))

        amount += sum(hl * (i - j - 1) for (hh, j), (hl, i) in zip(stack, stack[1:]))
        return amount - blocks

# @lc code=end

