class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # similar to 300 and 516
        # we can use 2d dp to solve this problem
        # lc cn solution https://leetcode-cn.com/problems/longest-common-subsequence/solution/zui-chang-gong-gong-zi-xu-lie-by-leetcod-y7u0/
        # use dp[i][j] to represent the longest common subsequence between text1[0:i] and text2[0:j]
        # if i=0 or j = 0, then dp[i][j] = 0
        # if text1[i-1] = text2[j-1], then dp += 1
        # else, choose the max between i-1, j or i, j-1
        
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)] # build a mxn 2d dp, +1 because 0 ot len
        
        for i in range(1, m+1): # start with 1 because dp[0] must be 0, and we need i-1 and j01
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]: # if equal, add one common subsequence to dp[i][j]
                    dp[i][j] = dp[i-1][j-1] + 1
                else: # if not equal, then choose
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n] 
    
    # time mn, space mn