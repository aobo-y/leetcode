#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        pre = dummy
        pre.next = head
        node = head

        while node and node.next:
            post = node.next

            pre.next = post
            node.next = post.next
            post.next = node

            pre, node = node, node.next

        return dummy.next


# @lc code=end

