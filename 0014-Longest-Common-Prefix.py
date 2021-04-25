class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for s in zip(*strs): # [f,f,f]
            if len(set(s)) >1:  # (f)
                return strs[0][:i]
            else:
                i += 1
        return strs[0][:i] if strs else ''

def test(strs):
    if len(strs) == 0:
        return ""
    res = strs[0]
    for i in range(len(strs)):
        while res not in strs[i]:
            res = res[0:len(res) - 1]
            if len(res) == 0:
                return ""
    return res