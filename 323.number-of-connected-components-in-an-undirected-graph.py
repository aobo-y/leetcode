#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        u = [i for i in range(n)]

        def head(i):
            if u[i] == i:
                return i
            u[i] = head(u[i])
            return u[i]

        def union(i, j):
            u[head(j)] = head(i)

        for i, j in edges:
            union(i, j)

        return sum(i == j for i, j in enumerate(u))

# @lc code=end

