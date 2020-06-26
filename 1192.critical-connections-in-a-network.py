#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edges = [set() for _ in range(n)]
        for a, b in connections:
            edges[a].add(b)
            edges[b].add(a)

        circle = set()
        # criticals = set{(a, b) for a, b in connections}

        def dfs(a, path, visited):
            visited.add(a)

            circle_origins = set()

            for b in edges[a]:
                if b in visited:
                    if b not in path or path[b] == a:
                        continue

                    circle_origins.add(b)
                    circle.add((a, b))

                else:
                    path[a] = b
                    co = dfs(b, path, visited)
                    if co:
                        circle.add((a, b))

                        if a in co:
                            co.remove(a)
                        circle_origins = circle_origins.union(co)

                    del path[a]

            return circle_origins

        dfs(0, {}, set())

        return [[a, b] for a, b in connections if (a, b) not in circle and (b, a) not in circle]


# @lc code=end

