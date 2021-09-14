from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # we could use dp, backtracing, dfs to solve this problem
        # https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
        # this question similar to 139, but we cannot know if a string can be break before we reach the end if we use 139 dp. Thus, we need a memo to record path
        
        ans = []
        
        def dfs(idx, path): # we need to record current idx and record all breakable word before idx
            if idx == len(s): # if we reach the end of string, means that this string can be break into senetences, so we add all recorded path into answer
                ans.append(' '.join(path)) # seperate with space
            
            for i in range(idx, len(s)):
                tmp = s[idx:i+1] # get a temp sentence and check if it in wordDict
                if tmp in wordDict:
                    dfs(i+1, path+[tmp]) # if yes, then continue dfs from idx i
            
        dfs(0, []) # start dfs from idx 0
        return ans
    
    """
    # dp solution by using lru to store cache
    
        @lru_cache(maxsize=None)
        def dp(i):
            res = []
            for word in wordDict:
                if word != s[i:i+len(word)]:
                    continue
                elif len(word) == len(s)-i:
                    res.append(word)
                else:
                    for sentence in dp(i+len(word)):
                        res.append(word + ' ' + sentence)        
            return res
        
        return dp(0)
    
        # backtracing solution, slowest
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []
    
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
    """
    # time complexity exponential, do not know exact time