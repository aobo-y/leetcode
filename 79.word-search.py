#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])

        def find_one(row_idx, col_idx, word_idx, path_set):
            if f'{row_idx} {col_idx}' in path_set:
                return False

            path_set.add(f'{row_idx} {col_idx}')

            if word_idx >= len(word):
                return True

            if row_idx < row_len - 1 \
                and board[row_idx + 1][col_idx] == word[word_idx] \
                and find_one(row_idx + 1, col_idx, word_idx + 1, path_set):
                return True

            if col_idx < col_len - 1 \
                and board[row_idx][col_idx + 1] == word[word_idx] \
                and find_one(row_idx, col_idx + 1, word_idx + 1, path_set):
                return True

            if row_idx > 0 \
                and board[row_idx - 1][col_idx] == word[word_idx] \
                and find_one(row_idx - 1, col_idx, word_idx + 1, path_set):
                return True

            if col_idx > 0 \
                and board[row_idx][col_idx - 1] == word[word_idx] \
                and find_one(row_idx, col_idx - 1, word_idx + 1, path_set):
                return True

            path_set.remove(f'{row_idx} {col_idx}')

            return False



        for row_idx, row in enumerate(board):
            for col_idx, val in enumerate(row):
                if val != word[0]:
                    continue

                word_idx = 1
                path_set = set()

                if find_one(row_idx, col_idx, 1, path_set):
                    return True

        return False



# @lc code=end

