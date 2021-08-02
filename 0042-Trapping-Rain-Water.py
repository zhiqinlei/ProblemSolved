class Solution:
    def trap(self, height: List[int]) -> int:
        # use two pointer to solve this problem
        # use leftmax and rightmax to record the hight left right hight of one line.
        # china lc solution
        
        leftMax = rightMax = 0
        left = 0
        right = len(height)-1
        
        ans = 0
        
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            
            if (leftMax <rightMax):
                ans += leftMax - height[left] # area = 1 * height
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
                
        return ans
    # O(n) Time, O(1) Space
