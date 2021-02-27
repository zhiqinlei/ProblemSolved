# BFS

from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        while queue:
            node, num = queue.popleft()
            if not node.left and not node.right:
                return num
            if node.left:
                queue.append((node.left, num +1))
            if node.right:
                queue.append((node.right, num +1))

#recursive dfs
def minDepth(self, root):
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1