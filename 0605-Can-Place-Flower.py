# 0605-Can-Place-Flower.py
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        s = len(flowerbed)
        for i in range(s):
            if flowerbed[i] == 0:
                if i == 0:
                    if s == 1 or flowerbed[i+1] == 0:
                        flowerbed[i] =1
                        n -= 1
    
                if i > 0 and i < s-1:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] =1
                        n -= 1
                
                if i == s-1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] =1
                        n -= 1       
                
        return n <= 0
            