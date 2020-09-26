#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
from collections import defaultdict
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        Trie = lambda: defaultdict(Trie)
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        trie = self.trie
        for c in word:
            trie = trie[c]
        trie[None] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        tries = [self.trie]
        for c in word:
            if c != '.':
                tries = [
                    trie[c] for trie in tries if c in trie
                ]
            else:
                tries = [
                    v for trie in tries for v in trie.values() if v
                ]

            if not tries:
                return False

        return any(None in trie for trie in tries)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

