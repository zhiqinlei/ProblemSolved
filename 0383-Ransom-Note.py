 # subtract counts of corresponding words, keeping non-negative values
 class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)
        return not len(ran - mag)