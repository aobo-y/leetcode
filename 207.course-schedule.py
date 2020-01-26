#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def cubic():
            pre_map = defaultdict(list)

            for edge in prerequisites:
                pre_map[edge[0]].append(edge[1])

            while pre_map:
                courses_able = []

                for course, pres in pre_map.items():
                    if all([p not in pre_map for p in pres]):
                        courses_able.append(course)

                if not courses_able:
                    return False

                for course in courses_able:
                    del pre_map[course]

            return True

        def bfs():
            graph = defaultdict(list)
            degrees = [0] * numCourses

            for edge in prerequisites:
                graph[edge[1]].append(edge[0])
                degrees[edge[0]] += 1

            able_set = set([i for i, v in enumerate(degrees) if v == 0])

            while able_set:
                new_able_set = set()

                for course in able_set:
                    for adj in graph[course]:
                        degrees[adj] -= 1
                        if degrees[adj] == 0:
                            new_able_set.add(adj)

                able_set = new_able_set

            return (not any(degrees))

        return bfs()



# @lc code=end

