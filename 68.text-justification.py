#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        line, line_len = [], 0
        for word in words:
            if line_len + len(word) + (1 if line else 0) > maxWidth:
                extra_spaces = maxWidth - line_len
                if len(line) == 1:
                    line.append(' ' * extra_spaces)
                else:
                    slots = len(line) // 2
                    per_slot = extra_spaces // slots
                    extra_slot = extra_spaces % slots

                    for i, idx in enumerate(range(1, len(line), 2)):
                        line[idx] += ' ' * per_slot
                        if i < extra_slot:
                            line[idx] += ' '

                res.append(''.join(line))
                line, line_len = [], 0


            if line:
                line.append(' ')
                line_len += 1

            line.append(word)
            line_len += len(word)

        extra_spaces = maxWidth - line_len
        res.append(''.join(line) + ' ' * extra_spaces)

        return res



# @lc code=end

