#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start
from collections import defaultdict
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        for f in folder:
            t = trie
            for c in f[1:].split('/'):
                t = t[c]
            t[None] = None

        res = []

        def dfs(t, path=[]):
            if None in t:
                res.append('/' + '/'.join(path))
                return

            for c, nt in t.items():
                path.append(c)
                dfs(nt, path)
                path.pop()

        dfs(trie)

        return res


# @lc code=end

