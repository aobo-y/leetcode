#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#

# @lc code=start
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        a_len, w_len = len(A), len(A[0])

        u = {a: a for a in A}

        def head(a):
            if u[a] == a:
                return a
            u[a] = head(u[a])
            return u[a]

        if a_len <= w_len ** 2:  # takes a_len ^ 2 * w_len
            for i in range(len(A) - 1):
                for j in range(i + 1, len(A)):
                    a1, a2 = A[i], A[j]
                    h1, h2 = head(a1), head(a2)
                    if h1 != h2 and sum(c1 != c2 for c1, c2 in zip(a1, a2)) <= 2:
                        u[h2] = u[h1]

        else:  # takes a_len * w_len ^ 3
            A = set(A)

            for a in A:
                cc = list(a)
                for i in range(len(cc) - 1):
                    for j in range(1, len(cc)):
                        cc[i], cc[j] = cc[j], cc[i]
                        t = ''.join(cc)
                        if t in A:
                            h1, h2 = head(a), head(t)
                            if h1 != h2:
                                u[h2] = u[h1]
                        cc[i], cc[j] = cc[j], cc[i]

        return sum(k == v for k, v in u.items())

# @lc code=end

