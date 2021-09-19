# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        # we can use recursive to solve this problem 
        # lc solution: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36984/An-inorder-python-solution
        """
        Do not return anything, modify root in-place instead.
        """
        
        """
        if not root:
            return
        self.prev = root
        self.flatten(root.left)

        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp

        self.flatten(temp)
        """
        
        
        """
                 *
                /
              n
            /     \
         left   right
          \ 
           *
            *
             \
              p
        The idea is very simple. Suppose n is the current visiting node, and p is the previous node of preorder traversal         to n.right.

        We just need to do the inorder replacement:

        n.left -> NULL

        n.right - > n.left

        p->right -> n.right
        
                 *
                /
              n
               \
               left
                 \ 
                  *
                   *
                    \
                     p
        """
        # a faster method
        # https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
        curr = root
        
        while curr:
            if curr.left != None:
                p = curr.left # p represent the prev node of right children node
                while p.right != None:
                    p = p.right
                    
                p.right = curr.right
                
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right
            # Time ON Space O1