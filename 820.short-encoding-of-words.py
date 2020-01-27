#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

# @lc code=start
from collections import defaultdict

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        words = set(words) # rm duplicates
        words = sorted(words, key=lambda w: len(w), reverse=True)
        length = 0

        for word in words:
            node = trie

            for l in word[::-1]:
                idx = ord(l) - ord('a')
                node = node[idx]

            if not len(node):
                length += len(word) + 1

        return length




# @lc code=end

