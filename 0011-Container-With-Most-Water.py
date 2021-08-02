class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use two pointer to solve
        left = 0
        right = len(height)-1
        ans = 0
        
        while left < right:
            area = min(height[left], height[right]) * (right - left) # find the max possible area, means find the lower line
            ans = max(ans, area) # record the max area in the record
            
            if (height[left] < height[right]): # remove the lower line and iterate, because it cannot be larger
                left += 1
            else:
                right -= 1
        return ans
    # O(n) Time O(1) Space
