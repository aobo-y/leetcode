#
# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
#

# @lc code=start
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    import random
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for _ in range(10):
            w = random.choice(wordlist)
            r = master.guess(w)

            if r == 6:
                return

            if r == -1:
                r = 0

            wordlist = [
                word for word in wordlist
                if sum(c1 == c2 for c1, c2 in zip(word, w)) == r
            ]

            # print(len(wordlist))

# @lc code=end

