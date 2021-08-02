class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        destination = len(nums)-1
        
        # if one stage can jump, every stage in its step distance can also jump, loop until find the longest distance
        for i in range(len(nums)): 
            if max_reach < i: return False # can never reach next stage
            if max_reach >= destination: return True
            max_reach = max(max_reach, i + nums[i]) # increase max distance
