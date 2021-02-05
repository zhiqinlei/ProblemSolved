class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        sign = 1
        i = 0
        while ( i < len(s) and s[i] == ' '):
            i+=1
        
        if i < len(s):
            if s[i] == "+":
                sign = 1
                i+= 1

            elif s[i] == "-":
                sign = -1
                i+= 1

        while (i < len(s) and s[i].isdigit()):
            ans = ans*10 + int(s[i])
            i += 1
            
        if sign == 1:
            if ans > pow(2,31)-1:
                return pow(2,31)-1
            else:
                return ans
        
        if sign == -1:
            if ans > pow(2,31):
                return -pow(2,31)
            else:
                return sign*ans
            
        return pow(2,31)-1 if ans > pow(2,31)-1 else sign*ans