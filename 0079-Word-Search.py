class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        m, n = len(board), len(board[0])
        if m == 0 or n == 0:
            return False
        
        def dfs(self, board, r, c, i):
            if i == len(word):
                return True
        
            if 0 <= r and r < m and 0<= c and c < n and word[i] == board[r][c]:
                tmp = board[r][c]
                board[r][c] = "#" # mark visited
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    newr, newc = r+dx, c+dy
                    if dfs(self, board, newr, newc, i+1) == True:
                        return True
                board[r][c] = tmp
            return False
        
        for r in range(m):
            for c in range(n):
                if dfs(self, board, r, c, 0):
                    return True
        return False

