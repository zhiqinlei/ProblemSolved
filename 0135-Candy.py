# 0135-Candy
class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        lst = []
        
        for i in range(len(ratings)):
            lst.append(1)
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                       lst[i] = lst[i-1] + 1
        
        for i in range(len(ratings)-2,-1,-1):
            
            if ratings[i] > ratings[i+1] and lst[i] <= lst[i+1]:
                       lst[i] = lst[i+1] +1
        
        ans = 0
        #print(lst)
        for i in lst:
            ans += i
        
        return ans