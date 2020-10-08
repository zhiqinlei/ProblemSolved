# 0104-Maximum-Depth-of-Binary-Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1 DFS method time O(n) space worst O(n) best O(logn)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        height = max(leftHeight, rightHeight)+1
        return height

# Solution 2 BFS method time O(n) Space O(n)
def maxDepth(self, root: TreeNode) -> int:
        height = 0
        if not root:
            return height
        queue = [root]
        while queue:
            nextlevel = []
            while queue:
                top = queue.pop()
                if top.left:
                    nextlevel.append(top.left)
                if top.right:
                    nextlevel.append(top.right)
            queue = nextlevel
            height+=1
        return height