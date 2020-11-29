#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def method_1():
            state = [0, float('-inf')]
            buy_state = 0
            for p in prices:
                wo_stock, w_stock = state

                n_w_stock = max(buy_state - p, w_stock)
                n_wo_stock = max(w_stock + p, wo_stock)

                buy_state = wo_stock

                state = [n_wo_stock, n_w_stock]

            return state[0]

        def method_2():
            states = [[0, None], [0, float('-inf')]]

            for p in prices:
                new_state = [
                    max(states[-1][0], states[-1][1] + p),
                    max(states[-1][1], states[-2][0] - p)
                ]
                states.append(new_state)

            return states[-1][0]

        return method_1()

# @lc code=end

