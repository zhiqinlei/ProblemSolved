# template solution
class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)

# concise solution
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        
        def dfs(target, index, path):
            if target < 0:
                return  # backtracking
            if target == 0:
                res.append(path)
                return 
            for i in range(index, len(candidates)):
                dfs(target-candidates[i], i, path+[candidates[i]])
        
        dfs(target, 0, [])
        return res

#genius solution
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(remain, combo, index):
            if remain == 0:
                result.append(combo)
                return
            for i in range(index, len(candy)):
                if candy[i] > remain:
                    # exceeded the sum with candidate[i]
                    break #the for loop
                
                dfs(remain - candy[i], combo + [candy[i]], i)
                
        candy = sorted(candidates)
        result = []
        dfs(target, [], 0)
        return result