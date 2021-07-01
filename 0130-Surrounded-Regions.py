class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        
        m = len(board)
        n = len(board[0])
        
        def dfs(i, j):
            if 0 <= i <m and 0 <= j <n and board[i][j] == "O":
                board[i][j] = "."
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x, y = i+dx, j+dy
                    dfs(x, y)
                
                
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == ".":
                    board[i][j] = "O"
