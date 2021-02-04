class Solution:
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
        return s[left+1:right]