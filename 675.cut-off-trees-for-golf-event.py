#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#

# @lc code=start
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0]) if forest else 0

        trees = [
            (forest[r][c], (r, c))
            for r in range(m)
            for c in range(n)
            if forest[r][c] > 1
        ]

        trees = sorted(trees)
        all_steps = 0
        ori= (0, 0)

        for _, target in trees:
            visited = {ori}
            layer = {ori}
            steps = 0

            found = False

            while layer:
                new_layer = set()

                for pos in layer:
                    if pos == target:
                        found = True
                        break

                    row, col = pos
                    for r_delta, c_delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        new_row = row + r_delta
                        new_col = col + c_delta

                        if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n or not forest[new_row][new_col]:
                            continue

                        new_pos = (new_row, new_col)

                        if new_pos not in visited:
                            visited.add(new_pos)
                            new_layer.add(new_pos)

                if found:
                    break

                steps += 1
                layer = new_layer

            if not found:
                return -1

            all_steps += steps
            ori = target

        return all_steps


# @lc code=end

