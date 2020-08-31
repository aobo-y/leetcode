#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    from collections import Counter
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def method_1():
            counts = Counter(tasks)
            indices = {t: float('-inf') for t in counts.keys()}

            i = 0
            while counts:
                max_t, max_c = None, 0
                for t, c in counts.items():
                    if i - indices[t] <= n:
                        continue

                    if c > max_c:
                        max_c = c
                        max_t = t

                if max_t:
                    indices[max_t] = i
                    counts[max_t] -= 1
                    if not counts[max_t]:
                        del counts[max_t]

                i += 1

            return i

        def method_2():
            counts = Counter(tasks)
            max_c = max(counts.values())
            n_max_c = sum(1 for k, v in counts.items() if v == max_c)
            if n_max_c > n:
                return len(tasks)
            return max(len(tasks), n_max_c + (n + 1) * (max_c - 1))

        return method_2()



# @lc code=end

