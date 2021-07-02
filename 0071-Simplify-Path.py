class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        
        for i in path:
            if i not in ['.', '..', '']:
                stack.append(i)
            else:
                if i == '..' and len(stack) != 0:
                    stack.pop()
        return '/' + '/'.join(stack)
