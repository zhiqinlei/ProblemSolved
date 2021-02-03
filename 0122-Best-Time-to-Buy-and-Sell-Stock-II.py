'''
The profit is the sum of sub-profits. Each sub-profit is the difference between selling at day j, and buying at day i (with j > i). The range [i, j] should be chosen so that the sub-profit is maximum:

sub-profit = prices[j] - prices[i]

We should choose j that prices[j] is as big as possible, and choose i that prices[i] is as small as possible (of course in their local range).

Let's say, we have a range [3, 2, 5], we will choose (2,5) instead of (3,5), because 2<3.
Now, if we add 8 into this range: [3, 2, 5, 8], we will choose (2, 8) instead of (2,5) because 8>5.

From this observation, from day X, the buying day will be the last continuous day that the price is smallest. Then, the selling day will be the last continuous day that the price is biggest.

Take another range [3, 2, 5, 8, 1, 9], though 1 is the smallest, but 2 is chosen, because 2 is the smallest in a consecutive decreasing prices starting from 3.
Similarly, 9 is the biggest, but 8 is chosen, because 8 is the biggest in a consecutive increasing prices starting from 2 (the buying price).
Actually, the range [3, 2, 5, 8, 1, 9] will be splitted into 2 sub-ranges [3, 2, 5, 8] and [1, 9].

We come up with the following code:

The time complexity is O(N), space complexity is O(5)
'''
def maxProfit(prices):
        buy = 0 
        sell = 0
        profit = 0
        i = 0
        n = len(prices)-1
        while (i < n):
            
            while (i < n) and(prices[i] >= prices[i+1]):
                i += 1
            buy = prices[i]
            
            while (i < n) and (prices[i] < prices[i+1]):
                
                i+=1
            sell = prices[i]
            
                
            profit += sell - buy
        return profit

print(maxProfit([1,2,3,4,5]))