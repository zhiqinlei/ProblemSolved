# shortest and simple
def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q
# Let me explain why p is q. It is just to return True if p==None and q==None else False.

# dfs + stack
def isSameTree(self, p, q):
    stack = [(p, q)]
    while stack:
        n1, n2 = stack.pop()
        if n1 and n2 and n1.val == n2.val:
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        elif not n1 and not n2:
            continue
        else:
            return False
    return True

# BFS with queue    
def isSameTree3(self, p, q):
    queue = [(p, q)]
    while queue:
        node1, node2 = queue.pop(0)
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
    return True