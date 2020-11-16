#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def find(w, i=0, p=None):
            if i >= len(w):
                return True

            if not p:
                for j, row in enumerate(board):
                    for k, v in enumerate(row):
                        if v != w[0]:
                            continue

                        row[k] = None
                        r = find(w, i + 1, (j, k))
                        row[k] = v
                        if r:
                            return True

                return False

            j, k = p
            for nj, nk in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                if 0 <= nj < len(board) and 0 <= nk < len(board[0]) and board[nj][nk] == w[i]:
                    board[nj][nk] = None
                    r = find(w, i + 1, (nj, nk))
                    board[nj][nk] = w[i]

                    if r:
                        return True

            return False

        return [word for word in words if find(word)]
# @lc code=end

