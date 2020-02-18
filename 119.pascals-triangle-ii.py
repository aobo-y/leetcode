#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        layer = []

        for i in range(rowIndex + 1):
            tmp = 1
            for j in range(1, i):
                layer[j], tmp = tmp + layer[j], layer[j]

            layer.append(1)

        return layer

# @lc code=end

