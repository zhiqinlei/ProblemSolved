class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # we can use dp to solve this problem
        # https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/zui-chang-hui-wen-zi-xu-lie-by-leetcode-hcjqp/
        # use 2d dp[i][j] to represent the longest Palindrome Sub between s[i] to s[j]
        # if s is a palindrome and a = b, then asb will be palindrome
        
        n = len(s)
        dp = [[0]*n for _ in range(n)] # initialize 2d dp
        
        for i in range(n-1, -1, -1): # since j must be larger than i, i do reverse loop
            dp[i][i] = 1 # all single ch is palindromic
            for j in range(i+1, n):
                dp[i][j] = 1 # initialize all dp[x][y]
                if s[i] == s[j]: # if a = b
                    dp[i][j] = dp[i+1][j-1] +2 # add 2 nums length
                else: # if s[i] != s[j] 
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j]) # then longest palindromic subseq must inside i+1 to j or i to j-1
        return dp[0][n-1] # last idx is n-1
    
    # time On2 Space On2