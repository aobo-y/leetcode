#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        nums = []
        d = 10

        while x != 0:
            nums.append(x % d)
            x //= d

        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1

        return True

# @lc code=end

