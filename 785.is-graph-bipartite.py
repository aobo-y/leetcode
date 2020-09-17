#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        sets = [set(), set()]
        def dfs(n, set_n=0):
            set_t = 1 - set_n

            if n in sets[set_n]:
                return True
            if n in sets[set_t]:
                return False

            sets[set_n].add(n)

            for t in graph[n]:
                if not dfs(t, set_t):
                    return False

            return True

        for i in range(len(graph)):
            if i not in sets[0] and i not in sets[1]:
                if not dfs(i, 0):
                    return False

        return True


# @lc code=end

