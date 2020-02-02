#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lt_head, ge_head = ListNode(None), ListNode(None)
        lt_tail, ge_tail = lt_head, ge_head

        node = head

        while node:
            if node.val < x:
                lt_tail.next = node
                lt_tail = lt_tail.next

            else:
                ge_tail.next = node
                ge_tail = ge_tail.next

            node = node.next

        lt_tail.next = ge_head.next
        ge_tail.next = None
        return lt_head.next

# @lc code=end

