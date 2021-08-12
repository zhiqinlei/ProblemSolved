class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
        # backtracing
        #https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.
        
        # j, k in the end, i before j
        i, j= len(nums)-1, len(nums)-1
        
        while i > 0 and nums[i-1] >= nums[i]: #decreasing 
            i -=1
        
            
        if i == 0: # nums are in descending order
            nums.reverse()
            return 
        
        k = i-1
        if i > 0: # if nums[j] > nums[i] find the index
            while nums[k] >= nums[j]:
                j-=1
            # when find the index, swap it to get the next greater num
            nums[j], nums[k] = nums[k], nums[j]
        
        # reverse the nums[j:]
        left, right = k+1, len(nums)-1
        
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1; right -=1
        # O(n) time, O(1) space
            
        
