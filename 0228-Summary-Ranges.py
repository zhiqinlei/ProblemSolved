class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # https://leetcode.com/problems/summary-ranges/discuss/63446/My-easy-to-understand-Python-solution
        # use two pointer to solve
        if not nums:
            return [] 
        
        res, i, start, = [], 0, 0 # range [start -> i]
        while i < len(nums)-1: # in case of out range
            if nums[i] + 1 != nums[i+1]: # not continue
                res.append(self.printRange(nums[start], nums[i])) # record range
                start = i+1                                          # get a new start, i+1 incase of start only add 1 each time
            i+= 1
        res.append(self.printRange(nums[start], nums[i])) # add the last range
        
        return res
    
    def printRange(self, left, right):
        if left == right:
            return str(left)
        else:
            return str(left) + "->" + str(right)
                # O(n) Time, O(n) Space
