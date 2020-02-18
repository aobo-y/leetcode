#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        a = None

        i, j = 1, n

        while i <= j:
            k = (i + j) // 2

            if isBadVersion(k):
                a = k
                j = k - 1
            else:
                i = k + 1

        return a

# @lc code=end

