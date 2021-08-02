class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use dp to solve this problem
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39743/Python-DP-solution-120ms
        buy1 = buy2 = float("inf")
        sell1 = sell2 = 0
        
        for price in prices:
            buy1 = min(buy1, price) # min the cost
            sell1 = max(sell1, price - buy1) # max the profit
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
        return sell2
    # O(n) time, O(1) space
