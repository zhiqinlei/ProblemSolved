class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for s in zip(*strs): # [f,f,f]
            if len(set(s)) >1:  # (f)
                return strs[0][:i]
            else:
                i += 1
        return strs[0][:i] if strs else ''