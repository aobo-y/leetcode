#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        links = {}
        get_root = lambda x: get_root(links[x]) if x in links else x

        for a, b in edges:
            a_root = get_root(a)
            b_root = get_root(b)

            if a_root == b_root:
                return [a, b]

            links[a_root] = b_root

        return []


# @lc code=end

