class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = set('aeiouAEIOU')
        s = list(s)
        l,r= 0, len(s)-1
        while l < r:
            if s[l] in vow and s[r] in vow:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -=1
            if s[l] not in vow:
                l += 1
            if s[r] not in vow:
                r -=1
        return ''.join(s)

'''
The idea is really simple. But I think my code is somewhat ugly in two ways:

Convert string to list then convert back
Pointer processing is verbose.
'''