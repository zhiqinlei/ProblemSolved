row, col = len(matrix), len(matrix[0])
left, right, up, down = 0, col - 1, 0, row - 1
while len(res) < row*col:
            for c in range(left, right+1):
                if len(res) <row*col:
                    res.append(matrix[up][c])
            for r in range(up+1, down+1):
                if len(res) <row*col:
                    res.append(matrix[r][right])
            for c in range(right-1, left, -1 ):
                if len(res) <row*col:
                    res.append(matrix[down][c])
            for r in range(down, up, -1 ):
                if len(res) <row*col:
                    res.append(matrix[r][left])
            left += 1
            right -=1
            up += 1
            down -=1
        return res

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        ans = []
        row, col = len(matrix), len(matrix[0])
        left, right, up, down = 0, col - 1, 0, row - 1
        while left <= right and up <= down:
            for c in range(left, right +1):
                ans.append(matrix[up][c])
            for r in range(up+1, down+1):
                ans.append(matrix[r][right])
            if left < right and up <down:
                for c in range(right-1, left, -1):
                    ans.append(matrix[down][c])
                for r in range(down, up, -1):
                    ans.append(matrix[r][left])
            left +=1
            right -=1
            up += 1
            down -=1
        return ans
