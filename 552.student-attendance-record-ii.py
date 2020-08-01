#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        state = [[1, 0, 0], [0, 0, 0]] # 0 A (0, 1, 2 L), 1 A (0, 1, 2 L)

        for _ in range(n):
            no_a = [sum(state[0]), *state[0][:2]]
            one_a = [sum(state[0]) + sum(state[1]), *state[1][:2]]
            state = [
                [v % (7 + 10 ** 9) for v in no_a],
                [v % (7 + 10 ** 9) for v in one_a]
            ]

        return (sum(state[0]) + sum(state[1])) % (7 + 10 ** 9)

# @lc code=end

