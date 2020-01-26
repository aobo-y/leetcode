#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degrees = [0] * n

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

            degrees[edge[0]] += 1
            degrees[edge[1]] += 1

        def quadratic(): # time limit exceeds
            next_nodes = [[i] for i in range(n)]
            visited = [set() for i in range(n)]

            depth = 0
            results = []

            while True:
                for i in range(n):
                    nodes = next_nodes[i]
                    visited[i].update(nodes)

                    layer = []

                    for node in nodes:
                        layer += [n for n in graph[node] if n not in visited[i]]

                    next_nodes[i] = layer

                    if not next_nodes[i]:
                        results.append(i)

                if results:
                    break

                depth += 1

            return results

        def remove_leaves():
            if n == 1:
                return [0]

            leaves = [i for i, v in enumerate(degrees) if v == 1]
            n_left = n

            while n_left > 2:
                new_leaves = []

                for node in leaves:
                    degrees[node] -= 1

                    for adj in graph[node]:
                        if degrees[adj] != 0:
                            degrees[adj] -= 1

                        if degrees[adj] == 1:
                            new_leaves.append(adj)

                n_left -= len(leaves)
                leaves = new_leaves

            return leaves

        return remove_leaves()



# @lc code=end

