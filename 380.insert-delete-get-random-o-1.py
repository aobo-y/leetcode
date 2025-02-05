#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.d = {}
        self.l = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val in self.d:
            return False

        self.d[val] = len(self.l)
        self.l.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val not in self.d:
            return False

        pos = self.d[val]
        del self.d[val]

        n_val = self.l.pop()
        if n_val != val:
            self.l[pos] = n_val
            self.d[n_val] = pos

        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return random.choice(self.l)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

