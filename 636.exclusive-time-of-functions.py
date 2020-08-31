#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n

        prev = 0
        stack = []
        for log in logs:
            idx, t, time = log.split(':')
            idx = int(idx)
            time = int(time)

            if t == 'start':
                if stack:
                    times[stack[-1]] += time - prev
                stack.append(idx)
                prev = time
            else:
                times[stack.pop()] += time - prev + 1
                prev = time + 1

        return times

# @lc code=end

