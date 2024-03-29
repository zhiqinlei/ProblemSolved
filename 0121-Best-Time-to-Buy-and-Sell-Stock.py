class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = 0
        hist_max = 0
        for i in range(1, len(prices)):
            cur_max = max(0, cur_max + prices[i] - prices[i-1])
            hist_max = max(hist_max, cur_max)
        return hist_max

'''
The logic to solve this problem is same as "max subarray problem" using Kadane's Algorithm. Since no body has mentioned this so far, I thought it's a good thing for everybody to know.

All the straight forward solution should work, but if the interviewer twists the question slightly by giving the difference array of prices, Ex: for {1, 7, 4, 11}, if he gives {0, 6, -3, 7}, you might end up being confused.

Here, the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) of the original array, and find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.
'''
