"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # since it in same level, similar to Binary Tree level order traversal problem
        # we can use cur and next to record each level
        if not root:
            return None
        
        cur = root
        next = root.left
        
        while next: # while it has a left node
            cur.left.next = cur.right # left node's next is right node
            if cur.next: # if cur has a neighbor node
                cur.right.next = cur.next.left
                cur = cur.next # go ot next node
            else: # no brother node
                cur = next
                next = cur.left
        return root
      
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37465/Python-Solution-With-Explaintion
