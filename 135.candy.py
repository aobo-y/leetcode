#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        def binary():
            candies = [0] * len(ratings)

            def give(left, right):
                if left == right:
                    candies[left] = 1
                    return

                idx = (left + right) // 2
                give(left, idx)
                give(idx + 1, right)

                while idx >= left and ratings[idx] > ratings[idx+1] and candies[idx] <= candies[idx+1]:
                    candies[idx] = candies[idx+1] + 1
                    idx -= 1


                while idx < right and ratings[idx] < ratings[idx+1] and candies[idx] >= candies[idx+1]:
                    candies[idx+1] = candies[idx] + 1
                    idx += 1

            give(0, len(candies) - 1)
            return sum(candies)

        def one_run():
            total = 0
            up, down = 0, 0
            prev_rate = float('-inf')

            for rate in ratings:
                if rate > prev_rate:
                    down = 0
                    up += 1
                    total += up
                    peak = up
                elif rate < prev_rate:
                    up = 1
                    down += 1
                    total += down
                    if peak == down:
                        peak += 1
                        total += 1
                else:
                    up, down, peak = 1, 0, 1
                    total += 1

                prev_rate = rate

            return total

        def two_run():
            lr = [0] * len(ratings)
            rl = [0] * len(ratings)

            lr[0], rl[-1] = 1, 1
            for i in range(1, len(ratings)):
                lr[i] = lr[i-1] + 1 if ratings[i] > ratings[i-1] else 1
                rl[-i-1] = rl[-i] + 1 if ratings[-i-1] > ratings[-i] else 1

            return sum(max(l, r) for l, r in zip(lr, rl))

        return two_run()


# @lc code=end

