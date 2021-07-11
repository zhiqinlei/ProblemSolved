class Solution:
    def mySqrt(self, x: int) -> int:
        # use binary search solution, time complexity is O(logn)
        if x == 0 or x == 1: # exceptions
            return x
        
        l,r = 0, x
        while l < r:
            mid = (r+l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid
                
# https://leetcode.com/problems/sqrtx/discuss/25061/Python-binary-search-solution-(O(lgn)).
