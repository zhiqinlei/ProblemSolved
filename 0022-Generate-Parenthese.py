class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation
        # we can use dfs to solve 
        
        if not n:
            return []
        
        left, right, ans, path = n, n, [], ""
        
        self.dfs(left, right, ans, path)
        return ans
        
    def dfs(self, left, right, ans, path):
        if right < left: # not balance
            return
        if not right and not left: # 0, 0 add path to ans
            ans.append(path)
            return 
        if left: # left first
            self.dfs(left-1, right, ans, path+"(")
        if right:
            self.dfs(left, right-1, ans, path + ")")
            
    """
    visualize
    dfs(2, 2, [], "")
        dfs(1, 2, [], "(")
                dfs(0, 2, [], "((")
                        dfs(0, 1, [], "(()")
                                dfs(0, 0, [], "(())") # We got "(())" and we append it to ans
                dfs(1, 1, ["(())"], "()")
                        dfs(0, 1, ["(())"], "()(")
                                dfs(0, 0, ["(())"], "()()") # We got "(())" and we append it to ans
                        dfs(1, 0, ["(())", "()()"], "())") # will just return as right < left
        dfs(2, 1, ["(())", "()()"], ")") # will just return as right < left

    """