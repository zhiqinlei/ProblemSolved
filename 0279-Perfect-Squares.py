#simple BFS solution
class Solution:
    def numSquares(self, n: int) -> int:
        
        s = [i*i for i in range(1, int(math.sqrt(n)+1))] # square num <= n
        level = 0 # BFS level
        cur_l = {0} # list of numbers in BFS level 1
        
        while True:
            next_l = set()
            for a in cur_l:
                for b in s:
                    if a+b == n: 
                        return level +1
                    if a+b < n:
                        next_l.add(a+b)
            cur_l = next_l
            level += 1