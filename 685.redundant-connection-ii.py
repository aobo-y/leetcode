#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parents = defaultdict(list)
        tos = defaultdict(list)

        for f, t in edges:
            if f not in parents:
                parents[f] = []
            parents[t].append(f)
            tos[f].append(t)

        node = None
        for i, ps in parents.items():
            if len(ps) == 0:
                node = i

        path = []
        visited = set()
        def dfs(node):
            if node in visited:
                return node

            path.append(node)
            visited.add(node)

            for t in tos[node]:
                r = dfs(t)
                if r:
                    return r

            path.pop()
            return None

        if node:
            r = dfs(node)
        else:
            for node in parents.keys():
                r = dfs(node)
                if r:
                    break
                tos[node] = [] # remove path leads to no circle

        if r in path:
            circle = set(path[path.index(r):])

            if len(parents[r]) > 1: # two parent node
                for p in parents[r]:
                    if p in circle:
                        return [p, r]
            else:
                for f, t in edges[::-1]:
                    if f in circle and t in circle:
                        return [f, t]
        else:
            return [parents[r][-1], r]


# @lc code=end

