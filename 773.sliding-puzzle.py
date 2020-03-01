#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        to_key = lambda b: ''.join([''.join(str(n) for n in r) for r in b])

        visited = set()

        states = set([to_key(board)])
        steps = 0

        while states:
            new_states = set()

            for state in states:
                if state == '123450':
                    return steps

                visited.add(state)
                pos = state.index('0')
                row, col = pos // n, pos % n

                for move_row, move_col in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    t_row, t_col = row + move_row, col + move_col
                    if t_row < 0 or t_row >= m or t_col < 0 or t_col >= n:
                        continue

                    new_state, t_pos = state, t_row * n + t_col
                    new_state = [c for c in state]
                    new_state[pos], new_state[t_pos] = new_state[t_pos], new_state[pos]
                    new_state = ''.join(new_state)

                    if new_state not in visited:
                        new_states.add(new_state)

            states = new_states
            steps += 1

        return -1


# @lc code=end

