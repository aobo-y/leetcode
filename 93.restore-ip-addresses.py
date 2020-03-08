#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []

        ips = [[] for _ in s]

        for i in range(len(s)):
            for k in range(3):
                if i < k:
                    break

                token = s[i-k:i+1]
                if int(token) > 255 \
                    or (len(token) > 1 and token[0] == '0'): # 001 02 000
                    continue

                if i - k == 0:
                    ips[i].append([token])
                else:
                    for tokens in ips[i-k-1]:
                        if len(tokens) < 4:
                            ips[i].append([*tokens, token])

        return [
            '.'.join(token for token in tokens)
            for tokens in ips[-1] if len(tokens) == 4
        ]





# @lc code=end

