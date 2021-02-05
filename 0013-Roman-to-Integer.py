class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if s[i] == "I":
                if i <len(s)-1 and (s[i+1] == "V" or s[i+1] == "X"):
                    ans += -1
                else:
                    ans += 1
                    
            if s[i] == "V":
                ans += 5
                
            if s[i] == "X":
                if i <len(s)-1 and (s[i+1] == "L" or s[i+1] == "C"):
                    ans += -10
                else:
                    ans += 10
            
            if s[i] == "L":
                ans += 50
            
            if s[i] == "C":
                if i <len(s)-1 and (s[i+1] == "D" or s[i+1] == "M"):
                    ans += -100
                else:
                    ans += 100
                    
            if s[i] == "D":
                ans += 500
                
            if s[i] == "M":
                ans += 1000
        
        return ans