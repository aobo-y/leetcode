#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
from collections import Counter
import random
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # negate the counts to sort in ascending order with respect to both counts and word alphabetic rules
        counts = [(-c, w) for w, c in Counter(words).items()]

        def partial_quicksort(l, r, n):
            if l + 1 >= r:
                return

            pivot_idx = random.randint(l, r - 1)
            counts[pivot_idx], counts[r - 1] = counts[r - 1], counts[pivot_idx]
            pivot = counts[r - 1]

            ptr = l
            for i in range(l, r):
                t = counts[i]

                if t < pivot:
                    if i != ptr:
                        counts[ptr], counts[i] = counts[i], counts[ptr]
                    ptr += 1

            counts[r - 1], counts[ptr] = counts[ptr], counts[r - 1]

            if ptr - l + 1 < n:
                partial_quicksort(ptr + 1, r, n - (ptr - l + 1))

            partial_quicksort(l, ptr, min(k, ptr - l))

        partial_quicksort(0, len(counts), k)

        return [w for _, w in counts[:k]]


# @lc code=end

