# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        # find the last element and the length of Linkedlist
        lastElement = head
        length = 1
        
        while (lastElement.next):
            lastElement = lastElement.next
            length += 1
        
        # if k > length, k = k % length
        k = k % length
        
        # make it a circle
        lastElement.next = head
        
        # travel the linkedlist and cut it at length - k th node
        tempNode = head
        for _ in range(length - k - 1):
            tempNode = tempNode.next
        
        # the Node be cuted is the last node, its next is the head
        ans = tempNode.next
        tempNode.next = None
        return ans
        
        #https://leetcode.com/problems/rotate-list/discuss/348197/96-faster-Simple-python-solution-with-explanation
