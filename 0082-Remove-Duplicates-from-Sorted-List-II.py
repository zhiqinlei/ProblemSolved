# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur and cur.next and cur.next.val == cur.val:
                    cur = cur.next
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next
