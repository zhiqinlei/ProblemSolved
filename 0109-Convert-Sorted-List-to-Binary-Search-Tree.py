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
        if not head.next:
            return TreeNode(head.val)
        # we can use recursive to find the mid point
        # two pointer slow, fast
        slow, fast = head, head.next.next # fast is two step ahead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next # find the mid point
        slow.next = None # cut the child
        
        root = TreeNode(mid.val) # set the root
        root.left = self.sortedListToBST(head) # recursive to calculate left node
        root.right = self.sortedListToBST(mid.next)
        
        return root
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/35474/Python-recursive-solution-with-detailed-comments-(operate-linked-list-directly).
