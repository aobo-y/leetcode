#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def trick():
            node = headA
            while node:
                node.val = str(node.val)
                node = node.next

            node = headB
            while node:
                if type(node.val) == str:
                    break
                node = node.next

            inter = node

            node = headA
            while node:
                node.val = int(node.val)
                node = node.next

            return inter

        def method():
            l1, node = 0, headA
            while node:
                l1 += 1
                node = node.next
            l2, node = 0, headB
            while node:
                l2 += 1
                node = node.next

            if l1 < l2:
                l1, l2 = l2, l1
                nodeA, nodeB = headB, headA
            else:
                nodeA, nodeB = headA, headB

            for _ in range(l1 - l2):
                nodeA = nodeA.next

            while nodeA:
                if nodeA == nodeB:
                    return nodeA
                nodeA, nodeB = nodeA.next, nodeB.next

            return None


        return method()

# @lc code=end

