class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if i == 0:
                m = prices[i]
            else:
                if prices[i] - m > max_profit:
                    max_profit = prices[i] - m
                if prices[i] < m:
                    m = prices[i]
        return max_profit
            

