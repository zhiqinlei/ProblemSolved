class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/139609/python-iterative-and-recursive-solution
        # use recursive to solve
        if len(s) < k:
            return 0
        
        for ch in set(s): # avoid repeating num
            if s.count(ch) < k: # is a ch's num < k, it cannot be in the result, we could use it to split s
                return max(self.longestSubstring(clip, k) for clip in s.split(ch))
        return len(s)
    # O(n) Time, O(1) space
