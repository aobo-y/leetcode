#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        unvisited = set(wordList)

        if endWord not in unvisited:
            return 0

        if beginWord in unvisited:
            unvisited.remove(beginWord)
        layer = {beginWord}
        l = 1

        while layer:
            l += 1
            new_layer = set()
            for word in layer:
                for i in range(len(word)):
                    for j in range(26):
                        new_word = word[:i] + chr(97 + j) + word[i+1:]
                        if new_word == endWord:
                            return l
                        if new_word in unvisited:
                            unvisited.remove(new_word)
                            new_layer.add(new_word)
            layer = new_layer

        return 0


# @lc code=end

