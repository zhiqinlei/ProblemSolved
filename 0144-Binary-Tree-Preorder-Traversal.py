# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == []:
            return []
        result = []
        stack = []
        cur = root
        
        while cur or stack:
            if not cur:
                cur = stack.pop()
            if cur:
                result.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
        return result

#I borrowed the idea from Iterative solution on Inorder traversal, which only pushes nodes from left on stack. For preorder, we only need to push right node on stack.