#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_idx = None

        for i, price in enumerate(prices):
            if buy_idx is None:
                buy_idx = 0
                continue

            if price < prices[buy_idx]:
                buy_idx = i
            elif price - prices[buy_idx] > max_profit:
                max_profit = price - prices[buy_idx]

        return max_profit

# @lc code=end

