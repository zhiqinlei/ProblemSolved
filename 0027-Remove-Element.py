class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for i in nums:
            if i != val:
                nums[l] = i
                l += 1
        
        return l