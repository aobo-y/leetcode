#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        cs = set([c for s in words for c in s])
        edges = {c: {t: 0 for t in cs} for c in cs}

        for i in range(1, len(words)):
            w1, w2 = words[i], words[i-1]

            found_diff = False
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if edges[c1][c2] == 1:
                        return ''
                    edges[c1][c2] = -1
                    edges[c2][c1] = 1

                    found_diff = True
                    break

            if not found_diff and len(w1) < len(w2):
                return ''


        for m in cs:
            for i in cs:
                for j in cs:
                    if edges[i][m] == edges[m][j] == 1:
                        if edges[i][j] == -1:
                            return ''
                        edges[i][j] = 1
                        edges[j][i] = -1
                    elif edges[i][m] == edges[m][j] == -1:
                        if edges[i][j] == 1:
                            return ''
                        edges[i][j] = -1
                        edges[j][i] = 1

        # for c, e in edges.items():
        #     print(c, e)
        ws = {c: sum(e.values()) for c, e in edges.items()}

        return ''.join(sorted(cs, key=lambda c: ws[c], reverse=True))


# @lc code=end

