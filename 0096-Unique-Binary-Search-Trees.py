class Solution:
    def numTrees(self, n: int) -> int:
        # https://leetcode.com/problems/unique-binary-search-trees/discuss/31826/Python-solutions-(DP-%2B-Catalan-number)
        # there are two solutions to solve
        
        # DP or math
        """
        ans = [0]*(n+1)
        ans[0] = 1
        
        for i in range(1, n+1): # i: 1->n
            for j in range(i): # j: 0->i-1
                ans[i] += ans[j] * ans[i-1-j]
                # For example, res[3] = res[0]*res[2]+res[1]*res[1]+res[2]*res[0]
#For each term on the RHS, the sum of index = index on LHS - 1
        return ans[i]
        """
# O(n2) time, O(n) space

# math solution Catalan Number  (2n)!/((n+1)!*n!)  
        return int(math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n))) # transfer to int
# O(n) time, O(1) space 
