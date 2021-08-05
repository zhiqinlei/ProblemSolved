class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # cn lc solution
        # use greedy and binary search to solve
        res = []
        
        for n in nums:
            if not res or n > res[-1]: # if find a num larger than the last element, just add
                res.append(n)
            else: # if not larger than the last, check if it is smaller than any element in res by using binary search
                left, right = 0, len(res)-1
                idx = right # idx of element larger than n, if not found, replace the last one
                while left <= right: # left <= right not <
                    mid = (left + right)//2
                    if res[mid] >= n: # find idx in res, not nums, must be >=
                        idx = mid
                        right = mid -1 # mid -1 not -=1
                    else:
                        left = mid + 1
                res[idx] = n # replace it
        return len(res)
    
    # O(nlogn) Time, O(n) Space
