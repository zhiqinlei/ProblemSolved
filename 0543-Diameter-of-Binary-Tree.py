# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node:
            return 0, -1 
        l_diam, l_path = self.helper(node.left)
        r_diam, r_path = self.helper(node.right)
        diam = max(l_diam, r_diam, 2+l_path + r_path)
        path = 1+max(l_path, r_path)
        return diam, path
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.helper(root)[0]

# https://leetcode.com/problems/diameter-of-binary-tree/discuss/101145/Simple-Python
