#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        cache = {}

        def find(i, j):
            if i >= l1 and j >= l2:
                return 0
            if i >= l1:
                return l2 - j
            if j >= l2:
                return l1 - i

            key = (i, j)
            if key not in cache:
                if word1[i] == word2[j]:
                    cache[key] = find(i + 1, j + 1)
                else:
                    cache[key] = min([
                        find(i + 1, j), # delete
                        find(i, j + 1), # add
                        find(i + 1, j + 1)
                    ]) + 1
            return cache[key]

        return find(0, 0)

# @lc code=end

