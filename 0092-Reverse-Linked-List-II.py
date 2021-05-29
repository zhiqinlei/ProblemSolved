# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre, cur = dummyNode, head
        
        for i in range(left -1):
            pre = pre.next
            cur = cur.next
        
        for i in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
            
        return dummyNode.next

#find linkedlist [left, right], reverse it, then connect 
#https://leetcode.com/problems/reverse-linked-list-ii/discuss/30672/Python-one-pass-iterative-solution
