#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = None
        node = head

        while node:
            if prev and node.val == prev.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return head


# @lc code=end

