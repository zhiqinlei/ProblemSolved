class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findtarget(nums, target):
            l,r = 0, len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] >= target:
                    r = mid -1
                else:
                    l = mid +1
            return l
        
        a = findtarget(nums, target)
        b = findtarget(nums, target+1)
        
        if a == len(nums) or nums[a] != target:
            return [-1,-1]
        else:
            return [a,b-1]
