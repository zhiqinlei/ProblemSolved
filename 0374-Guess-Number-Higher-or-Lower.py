class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1, n
        while l <= r: # only 1 num
            mid = (l+r)//2
            if guess(mid) ==0:
                return mid
            if guess(mid) == -1:
                r = mid -1
            else:
                l = mid +1
