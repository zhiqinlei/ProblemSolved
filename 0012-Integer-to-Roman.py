class Solution:
    def intToRoman(self, num: int) -> str:
        # use to dictionary to record symbol and value, from largest to smallest
        dic = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV",1:"I"} # use {} to represent dictionary
        
        ans = ""
        
        for value in dic:
            ans += num//value * dic[value]
            num %= value # 3010 % 1000 = 10
        return ans
