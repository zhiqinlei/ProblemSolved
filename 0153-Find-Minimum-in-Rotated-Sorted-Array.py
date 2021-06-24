class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high: # not <=
            pivot = (low+high) // 2
            if nums[pivot] < nums[high]:
                high = pivot # not pivot -1
            else:
                low = pivot +1
        return nums[low] # return low
