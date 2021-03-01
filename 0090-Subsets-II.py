#if S[i] is same to S[i - 1], then it needn't to be added to all of the subset, just add it to the last l subsets which are created by adding S[i - 1]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        cur = []
        n = len(nums)
    
        if not nums:
            return []
        
        nums.sort()
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                cur = [j + [nums[i]] for j in cur]
            else:
                cur = [j + [nums[i]] for j in ans]
            ans += cur
        return ans