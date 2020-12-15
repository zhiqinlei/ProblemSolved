# 28. Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
       
        for i in range(len(haystack)-len(needle)+1):
            num = 0
            for j in range(len(needle)):
                
                if haystack[i+j] == needle[j]:
                    
                    num += 1
            if num == len(needle):
                return i
        return -1