#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        paths = defaultdict(list)

        paths[endWord] = [[endWord]]

        words_to_visit = set([endWord])

        word_set = set(wordList)

        def next_words(word):
            for i in range(len(word)):
                for c in ascii_lowercase:
                    yield word[:i] + c + word[i+1:]

        while words_to_visit:
            if beginWord in words_to_visit:
                break

            new_word_to_visit = set()
            new_paths = defaultdict(list)

            for target_word in words_to_visit:
                for word in next_words(target_word):
                    if word == beginWord or (word in word_set and word not in paths):
                        new_word_to_visit.add(word)
                        new_paths[word] += [[word] + p for p in paths[target_word]]

            paths.update(new_paths)
            words_to_visit = new_word_to_visit

        return paths[beginWord]


# @lc code=end

