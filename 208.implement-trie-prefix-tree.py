#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
from collections import defaultdict
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        trie_node = lambda: defaultdict(trie_node)
        self.root = trie_node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            node = node[c]

        node['#'] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]

        return '#' in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]

        return bool(len(node))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

