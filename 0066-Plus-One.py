class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        
        for i in range(n, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits = [1] + digits
        return digits