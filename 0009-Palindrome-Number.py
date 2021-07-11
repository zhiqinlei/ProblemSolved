class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0 or (x > 0 and x % 10 == 0): # if x is negative or the last digit of positive x is 0
            return False
        
        reverseX = 0
        
        while x > reverseX:
            reverseX = reverseX*10 + x % 10
            x //= 10
        
        return (reverseX == x or x == reverseX//10)
    # if x is even, check reverse and x, else if x is odd check x == reverseX//10
    # https://leetcode.com/problems/palindrome-number/discuss/785314/Python-3-greater-1-solution-is-89.20-faster.-2nd-is-99.14-faster.-Explanation-added
