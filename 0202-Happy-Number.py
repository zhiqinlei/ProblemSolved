class Solution:
    def isHappy(self, n: int) -> bool:
        # key is to find visited number
        visited = set() # use set to record visited
        while n != 1:
            visited.add(n) # add it to visited
            n = sum(int(i)**2 for i in str(n)) # str(n) so it can iterate every digits
            if n in visited:
                return False # if found a circle
        return True
# https://leetcode.com/problems/happy-number/discuss/56915/My-Python-Solution
