#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head

        node = head
        mark = dummy
        val = None
        skip = True

        while node:
            if node.val != val:
                val = node.val

                if skip:
                    mark.next = node
                    skip = False
                else:
                    mark = mark.next
            else:
                skip = True

            node = node.next

        if skip:
            mark.next = None

        return dummy.next

# @lc code=end

