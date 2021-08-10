class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time).
        # https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/
        # use sort and two pointer to solve
        
        res = []
        nums.sort()
        # when i = 0, it doesn't need to check if it's a duplicate element since it doesn't even have a previous element to compare with. And nums[i] == nums[i-1] is to prevent checking duplicate again.
        for first in range(len(nums)-2): # len(nums)-2 is because we need at least 3 numbers to continue.
            
            if first > 0 and nums[first] == nums[first-1]:
                continue 
                
            
            second, third = first +1, len(nums)-1 # set two pointer, second on left, third on right
            
            while second < third:
                total = nums[first] + nums[second] + nums[third]
                
                if total < 0:
                    second += 1 # move right
                elif total > 0:
                    third -= 1
                else: 
                    res.append((nums[first], nums[second], nums[third]))
                    while second < third and nums[second] == nums[second+1]: # if same. left < right is important
                        second += 1
                    while second < third and nums[third] == nums[third-1]: # 
                        third -=1
                    second +=1; third -=1
        return res # watch out the scope !!!
            
        # O(n2) Time, O(logn) Space
        
                    
