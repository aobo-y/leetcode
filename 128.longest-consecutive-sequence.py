#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def method1():
            max_len = 0
            start_end = {}
            end_start = {}
            visited_nums = set()

            for num in nums:
                # have to skip duplicate nums
                if num in visited_nums:
                    continue

                visited_nums.add(num)

                if num + 1 in start_end:
                    end = start_end[num+1]
                else:
                    end = num

                if num - 1 in end_start:
                    start = end_start[num-1]
                else:
                    start = num

                length = end - start + 1

                start_end[start] = end
                end_start[end] = start

                if length > max_len:
                    max_len = length

            return max_len

        def method2():
            max_len = 0
            num_set = set(nums)

            while num_set:
                num = num_set.pop()
                length = 1

                i = 1
                while num + i in num_set:
                    length += 1
                    num_set.remove(num + i)
                    i += 1

                i = 1
                while num - i in num_set:
                    length += 1
                    num_set.remove(num - i)
                    i += 1

                if length > max_len:
                    max_len = length

            return max_len

        return method2()


# @lc code=end

