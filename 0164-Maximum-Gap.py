class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # use bucket sort to solve this problem 
        # https://leetcode.com/problems/maximum-gap/discuss/1240543/Python-Bucket-sort-explained
        
        ''''
        low, high, n = min(nums), max(nums), len(nums)
        
        if n <=2 or high == low: # avoid conor case 
            return high - low
        
        Bucket = defaultdict(list)
        for num in nums: # divide nums into n-1 buckets
            if num == high:
                ind = n-1
            else:
                ind = (num-low)*(n-1)//(high-low) # ith of bucket
            Bucket[ind].append(num) # add num into ith nums of bucket
        
        candidates = [[min(Bucket[i]), max(Bucket[i])] for i in range(n-1) if Bucket[i]] # min and max in ith bucket
        return max(y[0]-x[1] for x,y in zip(candidates, candidates[1:])) # max gap between buckets
        '''
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo: return hi - lo
        B = defaultdict(list)
        for num in nums:
            ind = n-2 if num == hi else (num - lo)*(n-1)//(hi-lo)
            B[ind].append(num)
            
        cands = [[min(B[i]), max(B[i])] for i in range(n-1) if B[i]]
        return max(y[0]-x[1] for x,y in zip(cands, cands[1:]))
        
        # O(n) Time, O(n) Space

