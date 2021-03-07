# dp easy to understand
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1) # dp[i] means s[:i] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True     
        return dp[-1]

'''
The idea is the following:

d is an array that contains booleans

d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example:

s = "leetcode"

words = ["leet", "code"]

d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

The result is the last index of d.
'''

#bfs or dfs
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from collections import deque
   		q = deque([s])
		seen = set() 
		while q:
            s = q.popleft()    # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
					if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False

'''
Starts with string s. For each string visited, chop off front of string if it starts with a word in the dictionary and adds the shortened string to the queue or stack. If string becomes empty, that means word break succeeded. Keep a set of seen string states to avoid duplicate work.
'''