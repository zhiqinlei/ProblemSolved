class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
        # we can use iterative and backtracing to solve
        res = []
        path = []
        self.dfs(s, path, res)
        return res
        
    def isPal(self, s): # check if s is palindrome
        return s == s[::-1]
    
    def dfs(self, s, path, res):
        if not s: 
            res.append(path)
            return # check all possibility
        for i in range(1, len(s)+1): # len(s)+1 not -1
            if self.isPal(s[:i]): # check inlice before i
                self.dfs(s[i:], path +[s[:i]], res) # recursivly find the rest, [s[:i]] not [[s[:i]]]
    
