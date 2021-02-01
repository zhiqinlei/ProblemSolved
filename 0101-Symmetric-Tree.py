# 0101-Symmetric-Tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        level = [root]
        while level:
            level_val = []
            tree_level = []
            for node in level:
                if node:
                    level_val.append(node.val)
                    tree_level.append(node.left)
                    tree_level.append(node.right)
                else:
                    level_val.append(None)
            if level_val != level_val[::-1]:
                return False
            level = tree_level
        return True