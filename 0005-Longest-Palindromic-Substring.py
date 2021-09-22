class Solution:
    # similar to dp solution
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            tmp = self.helper(s, i, i) #assume odd length, try to extend Palindrome as possible
            if len(tmp) > len(ans):
                ans = tmp
            tmp = self.helper(s, i, i+1) #assume even length.
            if len(tmp) > len(ans):
                ans = tmp
        return ans
    
    def helper(self, s, left, right):
        while left >=0 and right <len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right] # slice stop at right -1
        #The while loop stops either because l or r is out of range or because the s[l] != s[r], which means neither s[l] nor s[r] can be part of the longest palindrome and the helper function returns s[l+1:r](inclusive on the left and exclusive on the right).

        # Time O(n2) Space O1