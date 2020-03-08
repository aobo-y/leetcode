#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head

        i = 0
        start, rev_head = None, None
        node = dummy

        while node:
            next_node = node.next

            if i == m - 1:
                start = node
            elif i >= m and i <= n:
                node.next, rev_head = rev_head, node
                if i == m:
                    rev_tail = node

            i += 1
            node = next_node

            if i > n:
                break

        start.next = rev_head
        rev_tail.next = node

        return dummy.next

# @lc code=end

