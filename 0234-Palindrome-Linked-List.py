def isPalindrome(self, head):

    if not head or not head.next:
        return True

    # 1. Get the midpoint (slow)
    slow = fast = cur = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    
    # 2. Push the second half into the stack
    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    # 3. Comparison
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next
    
    return True

***
Here is the stack algorithm with O(N) time complexity and O(N/2) space complexity:

The algorithm has two steps:

Find the midpoint of the linked list
Push the second half values into the stack
Pop values out from the stack, and compare them to the first half of the linked list
The advantages of this algorithm are we don't need to restore the linked list and the space complexity is acceptable (O(N/2))
***
