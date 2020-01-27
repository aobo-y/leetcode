#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v

        def dfs(a, b, paths):
            if a not in graph or b not in graph:
                return -1.0

            if b not in graph[a]:
                ab = -1.0

                for c, ac in graph[a].items():
                    if c in paths or ac == -1.0:
                        continue

                    paths.add(c) # no need to remove from visited, coz if c cannot reach b, do not try c again
                    cb = dfs(c, b, paths)
                    if cb != -1.0:
                        ab = ac * cb
                        break

                graph[a][b] = ab
                graph[b][a] = 1 / ab

            return graph[a][b]

        return [
            dfs(a, b, set([a]))
            for a, b in queries
        ]




# @lc code=end

