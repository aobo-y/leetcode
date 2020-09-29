#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_1, max_profit_2 = 0, 0
        state = [float('-inf'), float('-inf')]  # init 2nd bought the same as 1st for buy only once

        for p in prices:
            s1, s2 = state

            # buy
            new_state = [max(-p, s1), max(max_profit_1 - p, s2)]

            # sell
            max_profit_1 = max(s1 + p, max_profit_1)
            max_profit_2 = max(s2 + p, max_profit_2)

            state = new_state

        return max_profit_2

# @lc code=end

