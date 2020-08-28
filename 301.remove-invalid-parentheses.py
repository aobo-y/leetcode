#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        s = s.lstrip(')').rstrip('(')

        opens, closes, letters = [], [], []

        i = 0
        while i < len(s):
            c = 0
            while i < len(s) and s[i] == '(':
                i += 1
                c += 1
            opens.append(c)
            j = i
            while i < len(s) and s[i] != ')' and s[i] != '(':
                i += 1
            letters.append(s[j:i])
            c = 0
            while i < len(s) and s[i] == ')':
                i += 1
                c += 1
            closes.append(c)

        o_to_rm, c_to_rm = 0, 0  # count to move
        for oc, cc in zip(opens, closes):
            o_to_rm += oc
            o_to_rm -= cc
            if o_to_rm < 0:
                c_to_rm -= o_to_rm
                o_to_rm = 0

        res = []
        def dfs(i, o=[], c=[], balance=0, o_rm=0, c_rm=0):
            if o_rm > o_to_rm or c_rm > c_to_rm:
                return

            if i == len(opens):
                if not balance:
                    res.append(''.join(
                        '(' * x + y + ')' * z
                        for x, y, z in zip(o, letters, c)
                    ))

                return

            oc, cc = opens[i], closes[i]

            #  either reduce open or close to achive minimum steps
            # from maximum possible n_cc to 0
            o.append(oc)
            for n_cc in range(min(cc, oc + balance), -1, -1):
                c.append(n_cc)
                dfs(i + 1, o, c, balance + oc - n_cc, o_rm, c_rm + cc - n_cc)
                c.pop()
            o.pop()

            # from all oc to minimum possible n_oc
            c.append(cc)
            for n_oc in range(oc - 1, max(0, cc - balance) - 1, -1):
                o.append(n_oc)
                dfs(i + 1, o, c, balance + n_oc - cc, o_rm + oc - n_oc, c_rm)
                o.pop()
            c.pop()

        dfs(0)
        return res



# @lc code=end

