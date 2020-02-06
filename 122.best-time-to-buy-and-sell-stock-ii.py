#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p, profit = None, 0

        for i, price in enumerate(prices):
            if i == len(prices) - 1:
                if p is not None:
                    profit += price - p
                break

            future_price = prices[i+1]

            if future_price > price and p is None:
                p = price
            elif future_price < price and p is not None:
                profit += price - p
                p = None

        return profit


# @lc code=end

