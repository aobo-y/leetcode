#
# @lc app=leetcode id=825 lang=python3
#
# [825] Friends Of Appropriate Ages
#

# @lc code=start
from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def binary_search():
            ages.sort()

            def count(a):
                i, j = 0, len(ages) - 1

                while i < j:
                    k = (i + j + 1) // 2
                    if ages[k] <= a:
                        i = k
                    else:
                        j = k - 1

                u = i

                v = a // 2 + 7
                i, j = 0, len(ages) - 1

                while i < j:
                    k = (i + j) // 2
                    if ages[k] <= v:
                        i = k + 1
                    else:
                        j = k

                l = i

                return u - l if l <= u else 0  # exclude itself

            return sum(count(a) for a in ages)

        def age_range():
            age_counts = Counter(ages)
            age_counts = sorted(age_counts.items())

            r = 0
            ptr = 0
            s = 0
            for a, c in age_counts:
                s += c

                pa = age_counts[ptr][0]
                while pa <= a * 0.5 + 7 and pa < a:
                    s -= age_counts[ptr][1]
                    ptr += 1
                    pa = age_counts[ptr][0]

                if a * 0.5 + 7 < a:
                    r += (s - 1) * c

            return r

        return age_range()


# @lc code=end

