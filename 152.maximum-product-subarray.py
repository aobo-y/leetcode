#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    # chop by 0, for odd neg, choose one side
    def maxProduct(self, nums: List[int]) -> int:
        first_neg_prod = None
        neg_count = 0
        max_prod = float('-inf')

        prod = 1

        for num in nums:
            prod *= num

            if num < 0:
                neg_count += 1

                if neg_count % 2 == 0:
                    prod *= first_neg_prod
                elif neg_count != 1:
                    prod = int(prod / first_neg_prod)

            if prod > max_prod:
                max_prod = prod

            if num == 0:
                first_neg_prod = None
                neg_count = 0
                prod = 1
            elif num < 0 and neg_count == 1:
                first_neg_prod = prod
                prod = 1

        return max_prod
# @lc code=end

