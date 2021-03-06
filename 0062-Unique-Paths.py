# 2d array dp solution
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #### DP solution ####
        
        # edge cases
        if m <= 0 or n <= 0:
            return 0
        if m == 1 or n == 1:
            return 1
        
        # build an empty matrix
        matrix = [[1 for j in range(n)]for i in range(m)]
        print(matrix)
        
        # record steps for each cell using DP (Expect the first row and the first column, since there are only one way to get the cells in these places..)
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[-1][-1]

# 1d array
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1] if m and n else 0
#If you see the original code a few times you'll see that after filling 'j'th row you won't really need the 'j-1'th row. So what you can do is overwrite aux[j-1] with aux[j]. In other words a single row is enough (it keeps getting overwritten). This brings space complexity down to O(n) from O(n*m)

# math C(m+n-2,n-1)
def uniquePaths1(self, m, n):
    if not m or not n:
        return 0
    return math.factorial(m+n-2)/(math.factorial(n-1) * math.factorial(m-1))
 
# O(m*n) space   
def uniquePaths2(self, m, n):
    if not m or not n:
        return 0
    dp = [[1 for _ in xrange(n)] for _ in xrange(m)]
    for i in xrange(1, m):
        for j in xrange(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

# O(n) space 
def uniquePaths(self, m, n):
    if not m or not n:
        return 0
    cur = [1] * n
    for i in xrange(1, m):
        for j in xrange(1, n):
            cur[j] += cur[j-1]
    return cur[-1]