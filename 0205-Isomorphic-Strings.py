# classic two dic
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for i in range(len(s)):
            if s[i] in sd and sd[s[i]] != t[i]:
                return False
            if t[i] in td and td[t[i]] != s[i]:
                return False
            sd[s[i]] = t[i]
            td[t[i]] = s[i]
            
        return True

# follow up
'''
I was given this question in an interview ytd. I got a followup which asks me to group the isomorphic strings as well

e.g.
input:
['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']

return:
[
['xyx'], 
['xyz', 'abc', 'def'], 
['aab', 'xxy']
]
'''
def groupIsomorphic(strs):
    def encode(s):
        d = {}
        encoded = []
        for c in s:
            if c not in d:
                d[c] = len(d)
            encoded.append(d[c])
        return str(encoded)

    groups = {}
    for s in strs:
        encoded = encode(s)
        if encoded not in groups:
            groups[encoded] = []
        groups[encoded].append(s)

    return list(groups.values())

print(groupIsomorphic(['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']))

# one line code
def isIsomorphic(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# more interesting solutions
def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
        
    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in xrange(256)], [[] for _ in xrange(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)
    
    def isIsomorphic3(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
    def isIsomorphic4(self, s, t): 
        return [s.find(i) for i in s] == [t.find(j) for j in t]
    
    def isIsomorphic5(self, s, t):
        return map(s.find, s) == map(t.find, t)

    def isIsomorphic6(self, s, t):
        d1, d2 = [0 for _ in xrange(256)], [0 for _ in xrange(256)]
        for i in xrange(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i+1
            d2[ord(t[i])] = i+1
        return True
