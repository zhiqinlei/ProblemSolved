# same to permutations except duplicate temp
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() #duplication
        
        def dfs(nums, path):
            if nums == []:
                ans.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: # duplication
                    continue # duplication
                dfs(nums[:i]+nums[i+1:], path + [nums[i]])
        dfs(nums, [])
        return ans