#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        node = head
        mark = head
        tail = None
        i = 0

        while k:
            while node:
                if i > k:
                    mark = mark.next

                tail = node
                node = node.next
                i += 1

            if k >= i:
                k = k % i
                i = 0
                node = head
            else:
                target = mark.next
                mark.next = None
                tail.next = head
                head = target
                break

        return head


# @lc code=end

