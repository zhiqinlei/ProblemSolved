class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # use dp to solve this problem
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: # start position
                    continue
                elif i == 0: # leftest col, only down
                    grid[i][j] += grid[i][j-1]
                elif j == 0: # top row, only right
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]
# https://leetcode.com/problems/minimum-path-sum/discuss/23466/Simple-python-dp-70ms
