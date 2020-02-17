#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        n, node = 0, head
        while node:
            n += 1
            node = node.next

        # find split
        h = (n + 1) // 2
        node1, node2 = head, head
        for i in range(h):
            node2 = node2.next

        # reverse
        prev = None
        while node2:
            prev, node2.next, node2 = node2, prev, node2.next
        node2 = prev

        # merge
        for i in range(h):
            node1.next, node1 = node2, node1.next
            if i != h - 1:
                node2.next, node2 = node1, node2.next


# @lc code=end

