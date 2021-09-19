class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        #we can use dp to solve this problem
        # cn lc solution: https://leetcode-cn.com/problems/stone-game-ii/solution/shi-zi-you-xi-qi-pi-lang-xi-lie-zhi-er-a-iucm/
        # dp[i][m] represent the max stone nums in range [i:n-1] when M = m
        # if current player pick in range [i:i+x-1], another player can only pick from [i+x-1: max(m,x)]
        # if i + 2M reach the end, i+2M > n, pick all remaining stones, dp[i][m] = sum[i:n-1]
        # else pick between dp[i][m] = max (dp[i][m], sum[i:n-1] - dp[i+x][max(M, x)]), X in range[1:2M]
        
        n = len(piles)
        preSum = 0 # use preSum to record sum[i:n-1]
        dp = [[0]*(n+1) for _ in range(n)] # dp [N][N+1]
        
        for i in range(n-1, -1, -1): # reverse loop
            preSum += piles[i] # record sum[i:n-1]
            for m in range(1, n+1):
                if (i+2*m >= n): # if i+2M reach the end
                    dp[i][m] = preSum # pick all remaining stones
                else: # if cannot pick all
                    for x in range(1, 2*m+1): # x in range [1:2m]
                        dp[i][m] = max(dp[i][m], preSum - dp[i+x][max(m, x)])
        
        return dp[0][1] # return max stones when m = 1 in range[0:n-1]