#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        l, node = 0, head
        while node:
            node = node.next
            l += 1

        if l == 1:
            return TreeNode(head.val)

        ll, node = 0, head
        while ll < l // 2 - 1:
            node = node.next
            ll += 1

        node.next, node = None, node.next

        treenode = TreeNode(node.val)

        if head != node:
            treenode.left = self.sortedListToBST(head)
        if node.next:
            treenode.right = self.sortedListToBST(node.next)

        return treenode

# @lc code=end

