class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        dic = defaultdict(int)
        for word in words:
            for ch in set(word):
                dic[word] |= (1<<(ord(ch)-97))
        
        for x in dic:
            for y in dic:
                if dic[x] & dic[y] == 0:
                    ans = max(ans, len(x)*len(y))
        return ans
#https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/1233802/Python-Bitmask-solution-explained
