class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # cn lc solution
        # use two point to solve
        # left fix, move right to right until find repeating, record length, move left to repeating num right
        # use dic to record seen
        
        seen_idx = {} # recored seen num and its idx, dic[key] = value
        key = -1 # use key to represent left pointer
        res = 0
        
        for idx, ch in enumerate(s): # idx as the right pointer
            if ch in seen_idx and seen_idx[ch] > key: # if find repeat, update left pointer
                key = seen_idx[ch] # move left to repeating num right
                seen_idx[ch] = idx
            else:
                seen_idx[ch] = idx
                res = max(res, idx - key )
        return res
    # O(n) Time, O(1) Space