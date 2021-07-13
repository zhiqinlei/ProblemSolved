# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.check(root) != -1 # -1 means not balanced
    
    def check(self, root): # use recursive to solve this problem
        if root == None:
            return 0
        left = self.check(root.left)
        right = self.check(root.right)
        
        if left == -1 or right == -1 or abs(left - right) >1: # if height diff larger than 1
            return -1
        
        return max(left, right) +1
# https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90
