#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def devide_sort(ary):
            if len(ary) <= 1:
                return ary, 0

            t = len(ary) // 2
            ary_s, c_s = devide_sort(ary[:t])
            ary_l, c_l = devide_sort(ary[t:])

            c = c_s + c_l
            i = 0
            for v_s in ary_s:
                c += i
                for j in range(i, len(ary_l)):
                    if v_s > ary_l[j] * 2:
                        i += 1
                        c += 1
                    else:
                        break

            a, b, ary = 0, 0, []
            while a < len(ary_s) and b < len(ary_l):
                s, l = ary_s[a], ary_l[b]
                if s <= l:
                    ary.append(s)
                    a += 1
                else:
                    ary.append(l)
                    b += 1

            ary += ary_s[a:] + ary_l[b:]
            return ary, c

        _, c = devide_sort(nums)

        return c

# @lc code=end

