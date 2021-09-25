class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # https://leetcode.com/problems/count-binary-substrings/discuss/1172569/Short-and-Easy-w-Explanation-and-Comments-or-Keeping-Consecutive-0s-and-1s-Count-or-Beats-100
        
        # need to find current consecutive and pre consecutive, find the min of them.
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]: # 01 or 10
                ans += min(prev, cur)
                prev = cur
                cur = 1
            else: # if consecutive, continue add cur
                cur += 1
        ans += min(prev, cur) # remember the last group
        return ans
    
    # Time O(n) Space O1