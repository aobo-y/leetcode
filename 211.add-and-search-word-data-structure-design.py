#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
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
            if not tries:
                break

            new_tries = []

            for trie in tries:
                if c == '.':
                    for c_ in trie.keys():
                        if c_ is not None:
                            new_tries.append(trie[c_])
                elif c in trie:
                    new_tries.append(trie[c])

            tries = new_tries

        return any(trie[None] is None for trie in tries)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

