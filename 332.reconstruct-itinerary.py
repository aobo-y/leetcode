#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for i, ticket in enumerate(tickets):
            graph[ticket[0]].append(ticket[1])

        for dests in graph.values():
            dests.sort()


        def find(paths):
            if len(paths) == len(tickets) + 1:
                return paths

            dept = paths[-1]
            dests = graph[dept]

            for i, dest in enumerate(dests):
                if not dest:
                    continue

                dests[i] = None

                found = find(paths + [dest])
                if found:
                    return found

                dests[i] = dest

        return find(['JFK'])





# @lc code=end

