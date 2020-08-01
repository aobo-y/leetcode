#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deps = [0] * numCourses
        pres = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            deps[a] += 1
            pres[b].append(a)

        res = []

        layer = [i for i, c in enumerate(deps) if c == 0]

        while layer:
            new_layer = []
            for i in layer:
                res.append(i)
                for j in pres[i]:
                    deps[j] -= 1
                    if not deps[j]:
                        new_layer.append(j)

            layer = new_layer

        return res if not any(deps) else []


# @lc code=end

