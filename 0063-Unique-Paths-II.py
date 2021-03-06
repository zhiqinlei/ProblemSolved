'''
DP[0][0] = 0 if s[0][0] = 1
DP[0][0] = 1 if s[0][0] = 0

DP[i][j] = 0 if s[i][j] = 1
DP[i][j] = DP[i-1][j] + DP[i][j-1]  if s[i][j] = 0
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        mat = [[0 for _ in range(c)] for _ in range(r)]
        mat[0][0] = 1 - obstacleGrid[0][0]
        
        for i in range(r):
            for j in range(c):
                if obstacleGrid[i][j] == 1:
                    mat[i][j] = 0
                else:
                    if i-1>=0:
                        mat[i][j] += mat[i-1][j]
                    if j-1>=0:
                         mat[i][j] += mat[i][j-1]
        
        return mat[-1][-1]

#DFS + DP
'''
This solution is just a variation of the standard solution provided by leetcode, but I think it's easier to understand. So basically the map is a acyclic directed graph, and we just need to find the total number of paths from start to end.

Normally DFS is sufficient for this kind of problem, however since we only need to report a single number, we can record the number of paths starting from a cell u once we completed the DFS starting from u. Next time when we hit u again, we know exactly the DFS result starting from u, so we don't have to do it again.

Note: lru_cache(doc) helps store the returned result of every distinct method call. It functions like a dict here, and you can also use a dict to do the same thing.

The time and space complexity are both O(MN).
'''

from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        
        @lru_cache(maxsize=None)
        def dfs(i, j):
            if obstacleGrid[i][j]:      # hit an obstacle
                return 0
            if i == M-1 and j == N-1:   # reach the end
                return 1
            count = 0
            if i < M-1:
                count += dfs(i+1, j)    # go down
            if j < N-1:
                count += dfs(i, j+1)    # go right
            return count
        
        return dfs(0, 0)