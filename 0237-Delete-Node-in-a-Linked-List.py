# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val
        node.next = node.next.next

# In node.val=node.next.val //We changed the value with the value of the node after it
        
#And then in node.next=node.next.next//We changed the next node with its next node to replace the next node's reference with the next node's.
