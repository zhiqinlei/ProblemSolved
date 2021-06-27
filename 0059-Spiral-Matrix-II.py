class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        
        matrix = [[ 0 for _ in range(n)] for _ in range(n)]
        left, right, up, down, num = 0,n-1,0,n-1,1
        while left <= right and up <= down:
            for c in range(left, right+1):
                matrix[up][c] = num
                num += 1
            up += 1
            for r in range(up, down+1):
                matrix[r][right] = num
                num += 1
            right -= 1
            for c in range(right, left-1, -1 ):
                matrix[down][c] = num
                num += 1
            down -=1
            for r in range(down, up-1, -1):
                matrix[r][left] = num
                num += 1
            left += 1
        return matrix
            
