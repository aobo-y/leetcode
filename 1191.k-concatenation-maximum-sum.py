#
# @lc app=leetcode id=1191 lang=python3
#
# [1191] K-Concatenation Maximum Sum
#

# @lc code=start
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        max_left, pos_appear = None, False

        sl, sr, sm, ml, mr, mm = 0, 0, 0, 0, 0, 0 # left right middle

        for i in range(len(arr)):
            vl = arr[i]
            vr = arr[-i - 1]

            sl = sl + vl
            sr = sr + vr

            if not pos_appear and vl > 0:
                pos_appear = True

            if pos_appear:
                sm += vl
                if sm < 0:
                    sm = 0
                mm = max(mm, sm)

            if sl > ml:
                ml = sl
                max_left = i

            mr = max(mr, sr)

        m = mm
        if k > 1:
            m = max(ml + mr + max(k - 2, 0) * max(0, sl), m)

        return int(m % (1e9 + 7))


# @lc code=end

