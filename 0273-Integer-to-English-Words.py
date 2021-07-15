class Solution:
    # divide interger by 3 digits, billion, million, thousand
    def __init__(self):
        self.lessthan20 = ["","One", "Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"] # first "" to avoid 0 index
        self.tenDigits = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"] # Forty, not Fourty
        self.thousands = ["","Thousand","Million","Billion"]
        # we dont not include hundreds because we divide interger by 3 digits
        
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        res = ""
        
        for i in range(len(self.thousands)):
            if num % 1000 != 0: # have number in thousands, from 1000 to 1 billion
                res = self.helper(num % 1000) + self.thousands[i] + " " + res # notice space
            num //= 1000 # divide 1000, less 3 digits
        return res.strip() # strip the space in the end
    
    def helper(self, num):
        if num == 0: # must have, incase 5050
            return ""
        if num < 20:
            return self.lessthan20[num] + " "
        elif num < 100:
            return self.tenDigits[num//10] + " " + self.helper(num%10) # must be helper
        else:
            return self.lessthan20[num//100] + " Hundred " + self.helper(num%100) 
# https://leetcode.com/problems/integer-to-english-words/discuss/70688/Python-Clean-Solution
