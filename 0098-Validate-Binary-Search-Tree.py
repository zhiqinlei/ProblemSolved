# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode, floor = float("-inf"), ceiling = float("inf")) -> bool:
        # Use recursive to solve this problem. add two parament floor and ceiling. 
        # all subtree must be larger than floor, be smaller than ceiling
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)
#https://leetcode.com/problems/validate-binary-search-tree/discuss/32178/Clean-Python-Solution
