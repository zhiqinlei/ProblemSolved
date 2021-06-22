***
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :
Input: [1,2,3]
Output: [1,2,4]
***

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        l = []
        while head != None:
            l.append(head)
            head = head.next
        i = len(l)-1
        while i >= 0:
            l[i].val += 1
            if l[i].val >= 10:
                l[i].val -= 10
                i -= 1
            else:
                break
        if i == -1:
            root = ListNode(x=1)
            root.next = l[0]
            return root
        else:
            return l[0]

# the time complexity is O(n), the spatial complexity is O(1)
