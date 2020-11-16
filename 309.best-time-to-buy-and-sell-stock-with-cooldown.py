#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        state = [0, float('-inf')]
        cooldown_wo_stock = 0
        for p in prices:
            wo_stock, w_stock = state

            n_w_stock = max(wo_stock - p, w_stock)

            n_wo_stock = max(cooldown_wo_stock, wo_stock)

            state = [n_wo_stock, n_w_stock]
            cooldown_wo_stock = w_stock + p

        return max(state[0], cooldown_wo_stock)

# @lc code=end

