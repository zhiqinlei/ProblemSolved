class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        ans = [[1],[1,1]]
        
        for level in range(1, numRows-1):
            last_level = ans[level]
            new_level = [1]
            for n in range(level):
                new_level.append(last_level[n]+ last_level[n+1])
            new_level.append(1)
            ans.append(new_level)
            
        
        return ans

# a genius short version by using map
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        for i in range(1, numRows):
            newline = map(add, [0] + res[-1], res[-1] + [0])
            res.append(list(newline))
        return res if numRows else []