class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ans = 0
        d = {} # use a dictionary to record length of file
        
        for f in input.splitlines(): # splitlines = split('\')
            depth = f.count('\t')    # count \t to record depths
            if '.' not in f:         # not a ext
                d[depth] = len(f) - depth # file length - \t
            else:                    # is ext
                cur = len(f) + sum(d[v] for v in range(depth)) # sum length + file length
                ans = max(cur, ans)
        return ans
