class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            pivot = (low + high) //2
            if nums[pivot] == nums[high]: # duplicate
                high -= 1
            elif nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot +1
        return nums[low]
