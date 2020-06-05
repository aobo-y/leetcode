#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        l, node = 0, root
        while node:
            l, node = l + 1, node.next

        c = l // k
        r = l % k

        res = []
        i, node = 0, root
        while len(res) != k:
            if i == 0:
                res.append(node)

            if node:
                i += 1

            next_node = node.next if node else None

            if i == c + (1 if r else 0):
                i = 0
                if r > 0:
                    r -= 1
                if node:
                    node.next = None

            node = next_node

        return res


# @lc code=end

