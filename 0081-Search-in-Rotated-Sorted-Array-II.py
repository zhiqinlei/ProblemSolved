class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        
        if n == 0:
            return False
        if n == 1:
            return nums[0] == target
        
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[l] and nums[mid] == nums[r]: # for duplicate
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]: # remember the elif, nums[l]
                if nums[l] <= target <nums[mid]: 
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return False
