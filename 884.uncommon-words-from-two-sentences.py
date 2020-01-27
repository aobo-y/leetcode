#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
from collections import Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        uc_words = Counter()

        for s in [A, B]:
            words = s.split(' ')
            for word in words:
                uc_words[word] += 1

        return [w for w, c in uc_words.items() if c == 1]

# @lc code=end

