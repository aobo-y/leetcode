#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s_ptr, f_ptr = head, head

        while f_ptr and f_ptr.next:
            f_ptr = f_ptr.next.next
            s_ptr = s_ptr.next

            if s_ptr == f_ptr:
                return True

        return False

# @lc code=end

