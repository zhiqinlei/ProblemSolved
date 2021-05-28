class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n /= 3
        return True if n == 1 else False

# one line code
        return n > 0 and pow(3, 32) % n == 0
