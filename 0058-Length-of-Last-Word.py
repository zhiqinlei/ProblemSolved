class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        if len(s) == 0:  #  so if s = '      '  (multiple spaces) then after splitting we can check the length which is zero
            return 0
        else:
            return len(s[-1])