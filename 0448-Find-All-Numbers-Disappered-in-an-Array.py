class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            tmp = abs(nums[i])-1
            if nums[tmp] > 0:
                nums[tmp] *= -1
            
        for i, n in enumerate(nums):
            if n > 0:
                ans.append(i+1)
        return ans

***
The idea is to use the original array to keep track of the numbers visited. Since all the numbers are positive intergers, for every number visited we mark the presence of that number by negating the number at the index equal to the current number. Since Python follows 0-indexing, the index we mark is actually number - 1. If the number at that index is already negated we do nothing. In the end, we just return the indices (index + 1 for the number) where there are still postive numbers.
***
