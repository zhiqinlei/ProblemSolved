# https://www.cnblogs.com/grandyang/p/5285868.html
# https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/286.html
# https://zhenyu0519.github.io/2020/03/07/lc286/
# lc plus
"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""
# use dfs or bfs to solve
class Solution:
   def wallsAndGates(self, rooms: List[List[int]]) -> None:
      if not rooms:
        return []
      row = len(rooms)
      col = len(rooms[0])
      directions = [(0,1), (0,-1), (1,0), (1,-1)]

      def dfs(x, y, dis):
        newx, newy = x+dx, y+dy
        if 0 < newx < row and 0< newy < col and rooms[x][y] < rooms[newx][newy]:
          rooms[newx][newy] = dis+1 # update distance val
          dfs(newx, newy, dis+1) # continue dfs
      
      for i in range(row):
        for j in rnage(col):
          if rooms[i][j] == 0: # if meet the door
            dfs(i, j, 0) # do dfs

"""
We iterate each cell will cost O(m*n) where m*n is the size of the 2D list. Each cell will also iterate four directions O(m*n*4). In total O(4*m*n)
"""




