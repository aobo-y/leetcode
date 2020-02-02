#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = len(lists)
        if l == 0:
            return None
        elif l == 1:
            return lists[0]
        elif l > 2:
            lists = [
                self.mergeKLists(lists[:l//2]),
                self.mergeKLists(lists[l//2:])
            ]

        head = ListNode(None)
        tail = head

        a, b = lists
        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next

            tail = tail.next
            tail.next = None

        tail.next = a if a else b
        return head.next


# @lc code=end

