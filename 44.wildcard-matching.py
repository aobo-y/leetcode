#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        cache = {}

        def match(s_ptr, p_ptr):
            key = (s_ptr, p_ptr)
            if key in cache:
                return cache[key]

            if p_ptr >= p_len:
                if s_ptr >= s_len:
                    cache[key] = True
                else:
                    cache[key] = False

                return cache[key]

            sc = s[s_ptr] if s_ptr < s_len else ''
            pc = p[p_ptr]

            if pc == '?':
                if not sc:
                    cache[key] = False
                else:
                    cache[key] = match(s_ptr + 1, p_ptr + 1)

            elif pc == '*':
                p_ptr += 1 # collapse continuous *
                while p_ptr < p_len and p[p_ptr] == '*':
                    p_ptr += 1

                while s_ptr <= s_len:
                    if match(s_ptr, p_ptr):
                        cache[key] = True
                        break
                    s_ptr += 1

                if key not in cache:
                    cache[key] = False

            else:
                if pc == sc:
                    cache[key] = match(s_ptr + 1, p_ptr + 1)
                else:
                    cache[key] = False

            return cache[key]

        return match(0, 0)





# @lc code=end

