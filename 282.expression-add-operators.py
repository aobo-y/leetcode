#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        def dfs(i, t, accum=1):
            res = []

            if i >= len(num):
                return res

            for j in range(i + 1, len(num) + 1 if num[i] != '0' else i + 2):
                token = num[i:j]
                v = accum * int(token)

                if j == len(num):
                    if v == t:
                        res.append(token)
                    continue

                add_res = dfs(j, t - v)
                for r in add_res:
                    res.append(f'{token}+{r}')

                min_res = dfs(j, t - v, -1)
                for r in min_res:
                    res.append(f'{token}-' + r)

                mul_res = dfs(j, t, v)
                for r in mul_res:
                    res.append(f'{token}*{r}')

            return res

        return dfs(0, target)

# @lc code=end

