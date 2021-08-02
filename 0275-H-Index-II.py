class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0; right = n -1
        while left <= right:
            mid = (left + right)//2
            if citations[mid] >= (n-mid): # n-mid nums paper be refered at least citations[mid] times
                right -=1
            else:
                left += 1
        return n - left  # not n - mid
    
    # time complexity: O(logn) binary search 
    # space complexity: O(1)
