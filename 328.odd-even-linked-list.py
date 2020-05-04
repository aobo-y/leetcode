#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        odd_head = odd_ptr = head
        even_head = even_ptr = head.next

        while odd_ptr.next and even_ptr.next:
            odd_ptr.next = odd_ptr.next.next
            if odd_ptr.next:
                odd_ptr = odd_ptr.next

            even_ptr.next = even_ptr.next.next
            if even_ptr.next:
                even_ptr = even_ptr.next

        odd_ptr.next = even_head
        return odd_head


# @lc code=end

