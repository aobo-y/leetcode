#
# @lc app=leetcode id=1320 lang=python3
#
# [1320] Minimum Distance to Type a Word Using Two Fingers
#

# @lc code=start
class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_cord(l):
            idx = ord(l) - 65
            return idx // 6, idx % 6

        def distance(x, y):
            if not x or not y:
                return 0

            xc, yc = get_cord(x), get_cord(y)
            return abs(xc[0] - yc[0]) + abs(xc[1] - yc[1])

        def recur():
            cache = {} # key = (f1, f2, next_word_idx)

            def min_dis(f1, f2, idx):
                if idx >= len(word):
                    return 0

                if f1 and (not f2 or ord(f1) > ord(f2)):
                    f1, f2 = f2, f1

                key = (f1, f2, idx)
                if key in cache:
                    return cache[key]

                dis = min(
                    distance(word[idx], f1) + min_dis(word[idx], f2, idx + 1),
                    distance(word[idx], f2) + min_dis(f1, word[idx], idx + 1)
                )

                cache[key] = dis
                return dis

            res = min_dis(None, None, 0)
            # print(cache)
            return res

        def dynam():
            layer = {(None, None): 0}

            for char in word:
                new_layer = {}
                for state, prev_dis in layer.items():
                    for i in range(2):
                        new_state = [*state]
                        new_state[i] = char
                        new_state = tuple(new_state)

                        dis = distance(char, state[i])

                        if new_state[0] and (not new_state[1] or ord(new_state[0]) > ord(new_state[1])):
                            new_state = (new_state[1], new_state[0])

                        if new_state not in new_layer:
                            new_layer[new_state] = prev_dis + dis
                        else:
                            new_layer[new_state] = min(new_layer[new_state], prev_dis + dis)

                layer = new_layer

            return min(layer.values())

        return dynam()


# @lc code=end

