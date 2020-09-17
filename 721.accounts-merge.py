#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts = [[a[0], set(a[1:])] for a in accounts]

        u = [i for i in range(len(accounts))]
        def head(i):
            if u[i] == i:
                return i
            u[i] = head(u[i])
            return u[i]

        def union(i, j):
            u[head(j)] = head(i)

        d = {}
        for i, (_, eset) in enumerate(accounts):
            for e in eset:
                if e not in d:
                    d[e] = i
                else:
                    union(i, d[e])

        for i in range(len(u)):
            h = head(i)
            if i != h:
                accounts[h][1] |= accounts[i][1]
                accounts[i][1] = None

        return [[n, *sorted(s)] for n, s in accounts if s]

# @lc code=end

