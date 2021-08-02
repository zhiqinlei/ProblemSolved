class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set() # use set to recored appeared num
        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        return False
    
    # time complexity O(n)
    # space O(n)
