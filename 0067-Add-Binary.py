'''
Addition
There are 3 basic rules for adding binary numbers:
0 + 0 = 0
0 + 1 = 1
1 + 1 = 10. If the sum of 2 bits is greater than 1, we need to shift a column on the left. In decimal system, 1 + 1 = 2. Binary notation of 2 is 10 (1 * 2^1 + 0 * 2^0). So we keep 0 in the 1's column and shift (carry over) 1 to the 2's column.
Other rules are same as the decimal system, i.e. we add from right to left and the carry over get’s added to the digits in the next column.
Now lets try adding 11 to 13. Binary for 11 is 1011 and that for 13 is 1101.
1011
+ 1101
1's col = 1 + 1 = 10. We keep 0 in 1's col and carry over 1 to 2's col.
2's col = 1 + 0 + 1 (carry over) = (1 + 0) + 1 = 1 + 1 = 10. Once again we keep 0 in 2's col and carry over 1 to 4's col.
4's col = 0 + 1 + 1 (carry over) = (0 + 1) + 1 = 1 + 1 = 10. Keep 0 in 4's col and carry over 1 in 8's col.
8's col = 1 + 1 + 1 (carry over) = (1 + 1) + 1 = 10 + 1 = 11. Keep 1 in 8's col and carry over 1 in 16's col.
The sum is 11000. 11000 = 1 * 2^4 + 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 0 * 2^0 = 16 + 8 + 0 + 0 + 0 = 24 = 11 + 13.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        
        a = list(a)
        b = list(b)
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result = str(carry%2) + result #new col first
            carry //= 2
            
        return result