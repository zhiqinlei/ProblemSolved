def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return left

# with duplicate
def searchInsert(self, nums, target): # works even if there are duplicates. 
    l , r = 0, len(nums)-1
    while l <= r:
        mid=(l+r)/2
        if nums[mid] < target:
            l = mid+1
        else:
            if nums[mid]== target and nums[mid-1]!=target:
                return mid
            else:
                r = mid-1
    return l
