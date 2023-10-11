class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrices = prices.copy()
        for i in range(len(prices)-2,-1,-1):
            maxPrices[i] = max(prices[i], maxPrices[i+1])
        
        maxProfit = 0
        for buyDay in range(len(prices)-1):
            buyPrice = prices[buyDay]
            sellPrice = maxPrices[buyDay+1]
            maxProfit = max(maxProfit, sellPrice-buyPrice)
        return maxProfit