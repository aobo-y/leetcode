#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dp():
            if len(s1) + len(s2) != len(s3):
                return False

            cache = [[None] * (len(s2) + 1) for _ in s1 + ' ']

            cache[0][0] = True

            for i in range(len(s1) + 1):
                for j in range(len(s2) + 1):
                    if i + j == 0:
                        continue

                    c = s3[i+j-1]

                    if (i > 0 and s1[i-1] == c and cache[i-1][j]) \
                        or (j > 0 and s2[j-1] == c and cache[i][j-1]):
                        cache[i][j] = True
                    else:
                        cache[i][j] = False


            return cache[-1][-1]

        def recur():
            if len(s1) + len(s2) != len(s3):
                return False

            cache = {}

            def check(ptr1, ptr2):
                key = (ptr1, ptr2)
                if key not in cache:
                    if ptr1 + ptr2 == len(s3):
                        res = True
                    elif ptr1 < len(s1) and s1[ptr1] == s3[ptr1+ptr2] and check(ptr1 + 1, ptr2):
                        res = True
                    elif ptr2 < len(s2) and s2[ptr2] == s3[ptr1+ptr2] and check(ptr1, ptr2 + 1):
                        res = True
                    else:
                        res = False

                    cache[key] = res

                return cache[key]

            return check(0, 0)

        return recur()

# @lc code=end

