#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        for d in digits:
            new_res = []
            res = res if res else ['']
            for ss in res:
                for c in m[d]:
                    new_res.append(ss + c)

            res = new_res

        return res


# @lc code=end

