lass Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num = 0
        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "#"
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    newx, newy = i+dx, j+dy
                    if 0 <= (newx) < m and 0<= (newy) <n:
                        dfs(newx, newy)
                return True
            return False
        
        for i in range(0, m):
            for j in range(0, n):
                if dfs(i, j):
                    num += 1
        
        return num
    
