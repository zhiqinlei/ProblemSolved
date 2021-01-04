# 455-Assign Cookies
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        
        child = 0
        cookie = 0
        while(child < len(g) and cookie < len(s)):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        
        return child