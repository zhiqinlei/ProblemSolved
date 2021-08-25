# https://medium.com/@rebeccahezhang/361-bomb-enemy-1b4b36d5a47a
# https://github.com/criszhou/LeetCode-Python/blob/master/361.%20Bomb%20Enemy.py

# lc plus

"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

For the given grid
0 E 0 0
E 0 W E
0 E 0 0
return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""

class Solution:
    def maxKilledEnemies(list grid):
# iterate thorugh the matrix by row and column
# if its '0', update the max so far by compare the current max
# and (enemies number in current row + enemies number in current column)
# becarefule the grid.length == 0 should be the first thing to check
# in case of array out of bound excetiopn happens on grid[0].length
        if (!grid or len(grid) == 0 or len(grid[0]) == 0):
            return 0
        
        m = len(grid)
        n = len(grid[0])
        maxnum = 0
        rowCount = 0
        colCount = [0]*n

        for i in range(m):
            for j in range(n):
# start from first row, count the enemies in the current row between two walls
# stroe it to avoid recompute
                if (j == 0 or gird[i][j-1] == 'W'):
# if on the edge
                    rowCount = 0
                    tmp = j
                    while (tmp < n and grid[i][tmp] != 'W'):
                        if (grid[i][k] == 'E'):
                            rowCount += 1
                        tmp += 1
# count the enmies in the row
                # start from column, count the enemies in the current vol between tow walls
                if (i == 0 or gird[i-1][j] == 'W'):
                    colCount[j] = 0
                    tmp = i
                    while (tmp < m and grid[tmp][j] != 'W'):
                        if (grid[tmp][j] == 'E'):
                            colCount[j]+= 1
                        tmp += 1
                # if this is a position to place the bomb, get the current max
                if (grid[i][j] == '0'):
                    maxnum = max(maxnum, rowCount + colCount[j])
       return maxnum
