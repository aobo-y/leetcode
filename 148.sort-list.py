#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sort(head):
            if not head:
                return None, None

            sm_head, lg_head = ListNode(None), ListNode(None)
            sm_tail, lg_tail = sm_head, lg_head

            pivot_head, pivot_tail = head, head
            node = head.next

            while node:
                if node.val > pivot_tail.val:
                    lg_tail.next, lg_tail = node, node
                elif node.val < pivot_tail.val:
                    sm_tail.next, sm_tail = node, node
                else:
                    pivot_tail.next, pivot_tail = node, node

                node = node.next

            sm_tail.next, lg_tail.next = None, None

            sm_head, sm_tail = sort(sm_head.next)
            lg_head, lg_tail = sort(lg_head.next)

            if sm_head:
                head, sm_tail.next = sm_head, pivot_head
            else:
                head = pivot_head

            pivot_tail.next = lg_head

            if lg_head:
                tail = lg_tail
            else:
                tail = pivot_tail

            return head, tail


        return sort(head)[0]
# @lc code=end

