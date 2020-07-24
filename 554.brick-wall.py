#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
class Solution:
    from collections import Counter
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = Counter()
        for row in wall:
            e = []
            l = 0
            for b in row[:-1]:
                l += b
                edges[l] += 1

        c = edges.most_common(1)[0][1] if edges else 0
        return len(wall) - c


# @lc code=end

