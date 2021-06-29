class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, m*n-1
        
        while l <= r:
            mid = (l+r)//2
            if matrix[mid//m][mid%m] == target:
                return True
            elif matrix[mid//m][mid%m] < target:
                l = mid +1
            else:
                r = mid -1
        return False
