class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use hashtable to solve, china lc solution
        seen = set(nums)
        longest_len = 0
        for num in seen:
            if num - 1 not in seen: # skip if num-1 already checked
                current_num = num
                current_len = 1
                
                while current_num +1 in seen: # is num +1 consecutive, find the consecutive sequence
                    current_num += 1
                    current_len += 1
                
                longest_len = max(longest_len, current_len) # find the longest consecutive sequence
        return longest_len
        
        
    # O(n) Time, O(n) Space
