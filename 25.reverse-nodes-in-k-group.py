#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head

        pre = dummy
        i = 1
        node = head

        while node:
            node = node.next

            if i == k:
                target = pre.next
                for _ in range(k - 1):
                    # rm shift
                    shift = target.next
                    target.next = shift.next
                    # insert shift
                    shift.next = pre.next
                    pre.next = shift

                pre = target
                i = 0

            i += 1

        return dummy.next

# @lc code=end

