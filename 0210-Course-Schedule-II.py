class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        ans = []
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        for node in range(numCourses):
            if not self.dfs(graph, visited, ans, node):
                return []
        return ans
    
    def dfs(self, graph, visited, ans, node):
        if visited[node] == -1:
            return False
        if visited[node] == 1:
            return True
        visited[node] = -1
        
        for j in graph[node]:
            if not self.dfs(graph, visited, ans, j):
                return False
        visited[node] = 1
        ans.append(node)
        return True
