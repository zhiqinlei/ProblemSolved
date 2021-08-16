class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # https://leetcode.com/problems/power-of-four/discuss/772269/Python-O(1)-oneliner-solution-explained
        # tricky, must use bit konwledge
        
        """How we can check that number is power of 4? Straightforward algorithm is to try to divide it by 4 and check if we have 1 after several divisions, but complexity of this approach will be O(log n). There is smarter way. To check that number is power of 4, we need to check 3 conditions:

Number is positive.
Number is power of 2.
This power of 2 is even power.
First condition is trivial. For the second condition we can use x&(x-1) trick, which removes the last significant bit of binary representation, for example 11010 & 11001 = 11000. Number is power of two if it have only one significant bit, that is after this operation it must be equal to zero.

The last part is a bit tricky. Hopefully if reached this step, we already know, that number is a power of 2, so we have not a lot of options left: 1, 10, 100, 1000, ... How we can distinguish one half of them (odd powers) from another half? The trick is to use binary mask m = 1010101010101010101010101010101. For even powers of 2 we have for example m&100 = 100, if we use odd power, for example m&1000 = 0."""
        
        return n > 0 and n &(n-1) == 0 and n & (0xAAAAAAAA) == 0
    """Actually the mask has 1 (set bit) in the odd positions while all even positions are 0 (unset bit), since we want to check if a number is power of four we want to make sure that no odd position has 1 (set bit) in our number, so using such a number as a mask which has 1 in all the odd positions up to 32 bits and performing a bitwise AND over it if results a 0, we are sure that our number is power of 4, and this mask is just a fancy way of denoting 0b1010.......10 (32 bits), because 0xA -> 0b1010 (hexadecimal to binary), hope I was clear enough.

"""
    # O(1) Time, O(1) Space
    
