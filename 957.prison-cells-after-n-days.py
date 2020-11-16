#
# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#

# @lc code=start
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        state = 0
        for i, v in enumerate(cells):
            state |= v << i

        cache = {}  # state: day
        states = []

        rec_idx = None

        for i in range(N):
            new_state = 0
            for j in range(1, 7):
                left = (1 << (j - 1) & state) != 0
                right = (1 << (j + 1) & state) != 0
                new_state |= (left == right) << j

            if new_state in cache:
                rec_idx = cache[new_state]
                break

            cache[new_state] = i
            states.append(new_state)
            state = new_state

        if rec_idx != None:
            rec = len(states) - rec_idx
            state = states[(N - 1 - rec_idx) % rec + rec_idx]

        return [int(1 << k & state != 0) for k in range(8)]

# @lc code=end

