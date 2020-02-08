#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        state = [n, n, ''] # open, close, str

        layer = [state]

        for _ in range(2 * n):
            new_layer = []

            for o, c, s in layer:
                if c > o:
                    new_layer.append([o, c - 1, s + ')'])
                if o > 0:
                    new_layer.append([o - 1, c, s + '('])

            layer = new_layer

        return [s[2] for s in layer]



# @lc code=end

