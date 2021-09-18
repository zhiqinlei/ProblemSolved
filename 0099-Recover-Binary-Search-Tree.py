# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # we can use stack inorder and morris inorder to solve this problem 
        # https://leetcode.com/problems/recover-binary-search-tree/discuss/187407/Python-short-and-slick-solution-(108ms-beats-100)-both-stack-and-Morris-versions
        # if we sort the bst inorder, there will be one or two disorder sequence. eg: 132 3>2 or 1432 4>3 3>2
        # we just need to swap these disorder num
        """
        stack inorder template
        
        def inorder(self, root):
            cur, stack = root, []
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left
            node = stack.pop()
            print(node.val)
            cur = node.right
        """
        """
        # stack inorder solution 
        cur, pre, swap, stack = root, TreeNode(float('-inf')), [], []
        # need pre to check sequence of cur and pre. swap to record disorder sequence
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.val < pre.val: # if disorder
                swap.append((pre, node)) # add the sequence into swap list
            pre, cur = node, node.right # move pre and cur into next node. must be node!
        
        swap[0][0].val, swap[-1][-1].val = swap[-1][-1].val, swap[0][0].val # remember .val it will work no matter adjacent or not
        
        # time ON space ON
        """
        
        """
        morris inorder template
        
        def inorderMorris(self, root):
            cur = root
            while cur:
                if cur.left:
                    temp = cur.left
                    while temp.right and temp.right != cur: 
                        temp = temp.right
                    if not temp.right:
                        temp.right, cur = cur, cur.left
                        continue
                    temp.right = None
                print(cur.val)
                cur = cur.right
        """
        
        cur, pre, swap, drop = root, TreeNode(float('-inf')), [], []
        while cur:
            if cur.left:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right, cur = cur, cur.left
                    continue
                tmp.right = None
            if cur.val < pre.val:
                swap.append((pre, cur))
            pre, cur = cur, cur.right
        swap[0][0].val, swap[-1][-1].val = swap[-1][-1].val, swap[0][0].val
        
        # time ON space O1