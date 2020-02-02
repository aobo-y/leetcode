#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def buffer():
            buffer = [None] * (n + 1)

            node, i = head, 0
            while node:
                buffer[i % (n + 1)] = node
                node = node.next
                i += 1

            pre = buffer[i % (n + 1)]
            target = buffer[(i + 1) % (n + 1)]
            post = target.next

            target.next = None
            if pre:
                pre.next = post
                head_ = head
            else:
                head_ = post

            return head

        def pointer():
            ptr = None

            node, i = head, 0

            while node:
                node = node.next
                i += 1
                if i == n + 1:
                    ptr = head
                elif i > n + 1:
                    ptr = ptr.next

            if ptr:
                target = ptr.next
                ptr.next = target.next
                head_ = head
            else:
                target = head
                head_ = head.next

            target.next = None
            return head_

        return pointer()





# @lc code=end

