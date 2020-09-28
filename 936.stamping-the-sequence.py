#
# @lc app=leetcode id=936 lang=python3
#
# [936] Stamping The Sequence
#

# @lc code=start
from collections import defaultdict
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        res = []
        c_idx = defaultdict(list)
        for i, c in enumerate(stamp):
            c_idx[c].append(i)

        def search(si, ti, w=0):
            if ti == len(target):
                if si == len(stamp):
                    res.append([w, ti - si])
                    return True
                else:
                    return False

            if si == len(stamp):
                for n_si in c_idx[target[ti]]:
                    n_w = 0 if n_si == 0 else w - 1
                    if search(n_si, ti, n_w):
                        res.append([w, ti - si])
                        return True
                return False

            if target[ti] == stamp[0] and si != 0:
                n_si, n_w = 0, w + 1
                if search(n_si, ti, n_w):
                    res.append([w, ti - si])
                    return True

            if target[ti] == stamp[si]:
                if search(si + 1, ti + 1, w):
                    return True

            return False

        if not search(0, 0):
            return []

        return [i for _, i in sorted(res)]

# @lc code=end

