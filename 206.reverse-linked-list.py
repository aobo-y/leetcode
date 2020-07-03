#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def iteratively():
            pre, node = None, head

            while node:
                node.next, node, pre = pre, node.next, node

            return pre

        def recursively():
            def reverse(pre, node):
                if not node:
                    return node

                rvs_head = reverse(node, node.next)
                node.next = pre
                return rvs_head if rvs_head else node

            return reverse(None, head)

        # return iteratively()
        return recursively()
# @lc code=end

