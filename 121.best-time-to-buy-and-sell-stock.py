#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for i, price in enumerate(prices):
            if price < min_price:
                min_price = min(price, min_price)
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

# @lc code=end

