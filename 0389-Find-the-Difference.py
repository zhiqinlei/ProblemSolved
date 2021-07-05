class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)
"""
    dictionary
    
    def findTheDifference(self, s, t):
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            if dic.get(ch, 0) == 0:
                return ch
            else:
                dic[ch] -= 1
                """
"""
class Solution(object):
    """
    xor
    """
    def findTheDifference(self, s, t):
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)
"""
