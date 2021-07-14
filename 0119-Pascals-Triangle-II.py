class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # same to Pascal's Triangle
        res = [[1]]
        
        for i in range(1, rowIndex+1): # must +1 or else out of range
            newline = map(add, [0]+res[-1], res[-1]+[0])
            res.append(list(newline))
        
        return res[rowIndex]
