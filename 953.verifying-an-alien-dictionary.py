#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}

        indices = [tuple(order_map[c] for c in w) for w in words]

        return all(indices[i] <= indices[i+1] for i in range(len(words) - 1))

# @lc code=end

