#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import Counter
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        res = Counter()
        def sts(node):
            if not node:
                return 0

            s = node.val
            if node.left:
                s += sts(node.left)
            if node.right:
                s += sts(node.right)

            res[s] += 1
            return s

        sts(root)
        max_ = float('-inf')
        r = []
        for v, c in res.items():
            if c > max_:
                r = [v]
                max_ = c
            elif c == max_:
                r.append(v)

        return r


# @lc code=end

