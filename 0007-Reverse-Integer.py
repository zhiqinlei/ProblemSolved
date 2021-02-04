class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        while x:
            r = r*10 + x%10
            x //= 10
        
        return 0 if r > pow(2, 31) else sign*r

# another way to hack it with int -> str ->int

def reverse(self, x):
        negFlag = 1
        if x < 0:
            negFlag = -1
            strx = str(x)[1:]
        else:
            strx = str(x)

        x = int(strx[::-1])
        
        return 0 if x > pow(2, 31) else x * negFlag