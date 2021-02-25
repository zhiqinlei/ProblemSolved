    # dfs + stack
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res
        
    # bfs + queue
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
        return res
        
    # dfs recursively
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res
    
    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)
			
    def binaryTreePaths1(self, root):
        return self.dfs(root, "")
    
    def dfs(self, root, path):
        if not root:
            return []
        path += str(root.val)
        if not root.left and not root.right:
            return [path]
        path += "->"
        return self.dfs(root.left, path) + self.dfs(root.right, path)
    
    def binaryTreePaths(self, root): # inorder
        stack, ret = [(root, "")], []
        while stack:
            node, path = stack.pop()
            if node:
                if not node.left and not node.right:
                    ret.append(path+str(node.val))
                s = path + str(node.val) + "->"
                stack.append((node.right, s))
                stack.append((node.left, s))    
        return ret

'''
An optimal solution is O(n * log(n)) time, where n is the number of nodes. In the worst case, the tree has (height ** 2) - 1 nodes and there are (n + 1) / 2 leaves. Each root-to-leaf path has length log(n + 1). A string must be created for each root-to-length path. Creating an m-length string requires O(m). (n + 1) / 2 leaves times log(n + 1) path length for each leaf equals O(((n + 1) / 2) * log(n)), which we say is equivalent to O(n * log(n)) for complexity analysis.

This solution is O(n * log(n) * log(n)). It concatenates strings at each step, where the combined string length is at most O(log(n + 1)). String concatenation for strings a and b is O(len(a) + len(b)). However, some Python implementations optimize string concatenation to O(1) in some cases. So, depending on the Python implementation, this solution might actually run in O(n * log(n)), but speaking generally, it is O(n * log(n) * log(n)).
'''