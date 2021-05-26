# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            root = TreeNode(root1.val+root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2

***
Let's create a recursive solution.

If both trees are empty then we return empty.
Otherwise, we will return a tree. The root value will be t1.val + t2.val, except these values are 0 if the tree is empty.
The left child will be the merge of t1.left and t2.left, except these trees are empty if the parent is empty.
The right child is similar.
***
