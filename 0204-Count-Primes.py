class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        # Sieve of Eratosthenes

        # We are only interested in numbers LESS than the input number
        # exit early for numbers LESS than 2; (two is prime)
        
        # create strike list for the input range, initializing all indices to
        # prime (1).
        
        prime = [1] * n
        # we know that 0 and 2 are not prime
        prime[0] = 0
        prime[1] = 0
        
        # Now set multiples of remaining numbers that are marked as prime to
        # not prime.  It is safe ignore numbers alreay marked as not prime
        # because there are factor(s) that divide evenly into this number and
        # all its multiples.  Use upper limit of (n**0.5)+1, because:
        #  (a) the smallest factor of a non-prime number will not be > sqrt(n).
        #      Ex. non-prime = 100, 
        #           5*20
        #           10*10, 
        #           20*5   # !! we have seen 5 before.
        
        for i in range(2, int(n**0.5) + 1): # n**0.5 maybe float
            if prime[i] == 1:
                # primes[i * i: n: i] = [False] * len(primes[i * i: n: i]) faster
                # 3x faster:
                # strikes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
                # n = 11
                # i = 2
                # (n-1-i*i)//i + 1
                # (n-1)               # get total # of indicies for n (non-inclusive)
                #     -i*i            # shift to get # of slots in range of interest
                #          //i        # get number of groups
                #              + 1    # get number of slots
                # strikes[2*2:11:2]  = [0] * ((11-1-2*2)//2 + 1
                # strikes[4:11:2]    = [0] * 4
                # s[4], s[6], s[8], s10] = 0, 0, 0, 0
                for j in range(i*i, n, i):
                    prime[j] = 0
        return sum(prime)
        # https://leetcode.com/problems/count-primes/discuss/153528/Python3-99-112-ms-Explained%3A-The-Sieve-of-Eratosthenes-with-optimizations
