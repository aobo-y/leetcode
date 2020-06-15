#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        token_lines = []

        number_lines, word_lines = [], []

        for line in logs:
            space_idx = line.index(' ')
            idf, content = line[:space_idx], line[space_idx+1:]

            if content[0].isdigit():
                number_lines.append(line)
            else:
                word_lines.append([line, idf, content])

        word_lines = sorted(word_lines, key=lambda t: (t[2], t[1]))

        word_lines = [line for line, _, _ in word_lines]

        return word_lines + number_lines

# @lc code=end

