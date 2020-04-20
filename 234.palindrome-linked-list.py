#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        slow, fast = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        node = slow
        prev = None
        while slow:
            slow.next, slow, prev = prev, slow.next, slow

        node1, node2 = head, prev

        while node1 and node2:
            if node1.val != node2.val:
                return False

            node1, node2 = node1.next, node2.next

        return True

# @lc code=end

