#0078-Subsets

#Given an integer array nums, return all possible subsets (the power set).

#The solution set must not contain duplicate subsets.

#Input: nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            #print("tmp: ", tmp)
            res.append(tmp)
            #print("res: ", res)
            for j in range(i, n):
                #print("[nums[j]] ", [nums[j]])
                helper(j+1, tmp + [nums[j]])
                
        helper(0,[])
        return res