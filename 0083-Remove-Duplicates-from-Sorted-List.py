# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        first, second = head, head.next
        
        while second:
            if first.val == second.val:
                second = second.next
                first.next = second
            else:
                first = second
                second = second.next
        
        return head
