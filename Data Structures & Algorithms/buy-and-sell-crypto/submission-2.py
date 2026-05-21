class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        result = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            result = max(result, prices[r]-prices[l])
        return result